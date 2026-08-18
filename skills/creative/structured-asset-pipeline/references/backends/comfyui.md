# Backend: ComfyUI (local)

## Env vars
- `COMFYUI_BASE_URL` (optional; default: `http://127.0.0.1:8188`)

## Allowed spec.params fields
`workflow_path` (absolute path to API-format workflow JSON — **required**), `prompt_node_ids` (list of node ids to inject prompt into; auto-detects CLIPTextEncode if absent), `negative_node_id`, `seed_node_id`, `seed`, `overrides` (dict of `node_id.field: value`)

## Prerequisites
ComfyUI must be running locally. Preflight: `GET /system_stats` — connection refused → exit 3 "Is ComfyUI running?"

## Exporting a workflow in API format

1. Open your workflow in the ComfyUI web UI.
2. Click the gear icon (Settings) → enable "Dev mode options".
3. Click "Save (API format)" — this saves a JSON file with node structure suitable for `/prompt`.
4. Place the JSON file somewhere accessible; put its absolute path in `spec.params.workflow_path`.

Note: The full UI export (`workflow.json` from "Save" without API format) is NOT compatible with `/prompt`. Always use API format.

## API flow
1. Load workflow JSON from `spec.params.workflow_path`
2. Inject `spec.prompt` into CLIPTextEncode node(s) identified by `prompt_node_ids` (or auto-detected)
3. `POST /prompt` with `{"prompt": graph, "client_id": uuid}`
4. Poll `GET /history/{prompt_id}` until entry appears with `outputs`
5. Find first `images` output; `GET /view?filename=…&subfolder=…&type=…`
6. Save to `--out`

## Cost
$0 — uses your local GPU. Latency is highly variable (seconds to minutes depending on model/steps/hardware).

## Failure modes
| Code | Meaning |
|------|---------|
| 1 | Missing workflow_path or path not found |
| 3 | Cannot connect to ComfyUI; poll timeout |
| 4 | Image written but verification failed |
