---
name: avalonia-port
description: Use when migrating a C# WinForms application to Avalonia UI for cross-platform support (Mac, Linux, Windows). Triggers on "port to Avalonia", "make this cross-platform", "WinForms to Avalonia", "add Mac support to C# app", "migrate WinForms", or any request to make a .NET desktop app run on macOS or Linux. Always use this skill before starting an Avalonia port — it encodes the full audit → abstraction → MVVM methodology.
---

# Avalonia Port

Methodology for migrating .NET WinForms applications to Avalonia UI.
Cross-platform: macOS (Apple Silicon + Intel), Linux, Windows.
Derived from MidsReborn-Mine port of Mids' Reborn Hero Designer.

---

## Phase 0 — Audit (before writing any Avalonia code)

### 1. Map WinForms contamination
```bash
# Core/business logic contamination:
grep -r "using System.Windows\|using System.Drawing\|System.Windows.Forms" ./Core --include="*.cs" -l

# Count total forms:
find ./UI/Forms -name "frm*.cs" ! -name "*.Designer.cs" | wc -l
```

### 2. Classify contamination by type

| Category | Example | Difficulty |
|---|---|---|
| `System.Drawing.Color` / `Bitmap` | Image rendering, color themes | **Easy** — replace with SkiaSharp (`SKColor`, `SKBitmap`) |
| `System.Drawing.Font` | Text rendering | **Easy** — replace with font abstraction interface |
| `System.Windows.Forms.MessageBox` | Error dialogs | **Medium** — replace with `IDialogService` |
| `System.Windows.Forms.Control` subclass | Custom controls | **Hard** — rewrite as Avalonia UserControl |
| `System.Drawing.Printing` | Print dialogs | **Hard** — replace with `IPrintService` |

**Key shortcut:** If SkiaSharp is already in the project (`SkiaSharp`, `SkiaSharp.Views.Desktop`), the `System.Drawing` → `SKColor`/`SKBitmap` migration is trivial. Check `.csproj` for existing SkiaSharp references first.

---

## Phase 1 — Create the Avalonia project (alongside, not replacing)

### Project file template
```xml
<Project Sdk="Microsoft.NET.Sdk">
  <PropertyGroup>
    <!-- net8.0 only — NO -windows suffix = runs on Mac, Linux, Windows -->
    <TargetFramework>net8.0</TargetFramework>
    <OutputType>WinExe</OutputType>
    <AvaloniaUseCompiledBindingsByDefault>true</AvaloniaUseCompiledBindingsByDefault>
  </PropertyGroup>
  <ItemGroup>
    <PackageReference Include="Avalonia" Version="11.2.3" />
    <PackageReference Include="Avalonia.Desktop" Version="11.2.3" />
    <PackageReference Include="Avalonia.Themes.Fluent" Version="11.2.3" />
    <PackageReference Include="Avalonia.Fonts.Inter" Version="11.2.3" />
    <PackageReference Include="Avalonia.ReactiveUI" Version="11.2.3" />
    <PackageReference Include="SkiaSharp.Views.Avalonia" Version="3.116.1" />
  </ItemGroup>
</Project>
```

### Directory structure
```
YourApp.Avalonia/
├── Views/          # .axaml + .axaml.cs per window/panel
├── ViewModels/     # ReactiveObject subclasses
├── Services/       # IDialogService, IImageProvider, IFileDialog abstractions
└── Assets/         # icons, fonts
```

### Entry point (Program.cs)
```csharp
using Avalonia;
using Avalonia.ReactiveUI;

class Program
{
    [STAThread]
    public static void Main(string[] args) =>
        BuildAvaloniaApp().StartWithClassicDesktopLifetime(args);

    public static AppBuilder BuildAvaloniaApp()
        => AppBuilder.Configure<App>()
            .UsePlatformDetect()   // auto-detects Mac/Linux/Windows
            .WithInterFont()
            .LogToTrace()
            .UseReactiveUI();
}
```

---

## Phase 2 — MVVM pattern (ReactiveUI)

Each WinForms form becomes a View + ViewModel pair:

| WinForms | Avalonia MVVM |
|---|---|
| `frmMain.cs` | `MainWindow.axaml` + `MainWindowViewModel.cs` |
| `frmStats.cs` | `StatsView.axaml` + `StatsViewModel.cs` |
| Direct field access `this.textBox1.Text = x` | `{Binding PropertyName}` in XAML, `RaiseAndSetIfChanged` in VM |
| `MessageBox.Show("error")` | `IDialogService.ShowError(message)` injected via constructor |

### Base ViewModel pattern
```csharp
using ReactiveUI;

public class MyViewModel : ReactiveObject
{
    private string _value = "";
    public string Value
    {
        get => _value;
        set => this.RaiseAndSetIfChanged(ref _value, value);
    }

    // Commands use ReactiveCommand, not event handlers
    public ReactiveCommand<Unit, Unit> LoadCommand { get; }

    public MyViewModel()
    {
        LoadCommand = ReactiveCommand.CreateFromTask(LoadAsync);
    }

    private async Task LoadAsync()
    {
        // business logic here, no UI references
    }
}
```

---

## Phase 3 — Core library extraction (optional but recommended for large apps)

If the original project has >5k lines of Core logic:
1. Create `YourApp.Core.csproj` targeting `net8.0` (no Windows suffix)
2. Move all Core files that pass `grep -L "System.Windows\|System.Drawing"` first
3. For contaminated files, introduce abstraction interfaces before moving:
   - `IColorPalette` instead of `System.Drawing.Color` usage
   - `IImageProvider` instead of `System.Drawing.Bitmap`
   - `IDialogService` instead of `MessageBox`
4. The Core project becomes a shared dependency of both WinForms (existing) and Avalonia (new) projects

---

## Phase 4 — MVP form selection

Port 5 forms first to validate the approach before committing to the full migration:
1. **Main shell** — the outer window frame (always first)
2. **Primary data view** — the most-used display panel
3. **Key picker dialog** — the modal users open most (item selection, file open)
4. **Settings/preferences** — confirms IDialogService, IFileDialog work
5. **Stats/output panel** — confirms data binding to computed values works

Validate each on macOS before porting the next.

---

## Package migration table

| WinForms package | Avalonia replacement |
|---|---|
| `SkiaSharp.Views.Desktop.Common` | `SkiaSharp.Views.Avalonia` |
| `SkiaSharp.Views.WindowsForms` | `SkiaSharp.Views.Avalonia` |
| `Microsoft.WinForms.Designer.SDK` | REMOVE (no visual designer needed) |
| `Costura.Fody` (embed DLLs) | REMOVE (use `dotnet publish --self-contained`) |
| `FontAwesome.Sharp` (WinForms) | `Material.Icons.Avalonia` or `Projektanker.Icons.Avalonia` |
| `Microsoft.Web.WebView2` | `Avalonia.WebView` |

---

## Running on Mac

```bash
cd YourApp.Avalonia/
dotnet run
# or publish as self-contained:
dotnet publish -r osx-arm64 --self-contained -o dist/mac-arm64
```

Requires: .NET 8 SDK — `brew install --cask dotnet-sdk`

---

## Common pitfalls

| Problem | Fix |
|---|---|
| `net8.0-windows` in .csproj | Change to `net8.0` — the Windows suffix locks you to Windows |
| WinForms `Control` in Core logic | Extract to `INavControl` interface; don't drag UI types into business logic |
| `Application.DoEvents()` in loops | Remove; use `async/await` with Avalonia's dispatcher |
| `Invoke()`/`BeginInvoke()` for thread marshalling | Use `Dispatcher.UIThread.Post(() => ...)` in Avalonia |
| `Graphics` / `OnPaint` custom drawing | Port to Avalonia `Canvas` + SkiaSharp `SKCanvas` via `SKXamlCanvas` |

---

## Alternative: web path (works on Mac today, no port needed)

If a full Avalonia port is too heavy, the LoadedCamel ecosystem already has a web approach:

| Repo | Role |
|---|---|
| [PowersAPI](https://github.com/LoadedCamel/PowersAPI) | Rust parser: CoH `.bin` files → JSON; live at coh.tips/powers/ |
| [hero-viewer](https://github.com/LoadedCamel/hero-viewer) | Electron app: reads `.mhd` builds, shows enhancement list; runs on Mac today |

**When to use web path instead of Avalonia:**
- Need Mac support *now* (not in 6+ months)
- Viewer-only is sufficient (no damage calc, no editing)
- Team has stronger JS than C# skills

**When to use Avalonia:**
- Need full editing + damage calculation (hero-viewer is read-only)
- Want a native app with OS file associations
- Plan to maintain parity with upstream Mids' feature set

---

## References

- [[midsreborn-mine]] — active port of Mids' Reborn (MidsReborn.Avalonia/)
- Avalonia docs: avaloniaui.net/docs
- ReactiveUI docs: reactiveui.net
- MidsReborn upstream 5.x Avalonia plan: github.com/LoadedCamel/MidsReborn
- hero-viewer (web alternative): github.com/LoadedCamel/hero-viewer
- PowersAPI (data layer): github.com/LoadedCamel/PowersAPI
