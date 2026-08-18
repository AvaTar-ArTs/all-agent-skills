const { execSync } = require('child_process');
const path = require('path');

const HERMES_DIR = path.join(process.env.HOME, '.hermes/hermes-agent');

function run(command) {
    try {
        console.log(`Running: ${command}`);
        execSync(command, { cwd: HERMES_DIR, stdio: 'inherit' });
    } catch (error) {
        console.error(`Error executing ${command}:`, error.message);
    }
}

const action = process.argv[2];

switch (action) {
    case 'start':
        run('docker-compose up -d');
        break;
    case 'stop':
        run('docker-compose stop');
        break;
    case 'status':
        run('docker-compose ps');
        break;
    case 'logs':
        run('docker-compose logs -f');
        break;
    case 'config':
        console.log('Syncing config...');
        // Implementation for config sync would go here
        break;
    default:
        console.log('Usage: hermes-manage [start|stop|status|logs|config]');
}
