# VPS Deployment & Domain Structure
**Last Updated**: 2026-01-01

## Server Access
- **Host**: `46.62.216.163`
- **User**: `arner`
- **Command**: `ssh arner@46.62.216.163`
- **Datacenter**: Hetzner Helsinki
- **App Directory**: `~/task_app/`

## Domains & Routes

| URL | Description | Source File |
|-----|-------------|-------------|
| `arnereabel.com` | Main portfolio website | `~/task_app/main_site/` |
| `tasks.arnereabel.com/` | Root (serves main_site) | `~/task_app/main_site/` |
| `tasks.arnereabel.com/welding/` | Three.js welding simulator | `~/task_app/welding/index.html` |
| `tasks.arnereabel.com/floorplan/` | Task distribution app | `~/task_app/floorplan/index.html` |

## Docker Setup

### Container Services
```
task_nginx   - Nginx frontend (port 80)
task_backend - Node.js API (port 3001)
```

### Key Files
```
~/task_app/
├── docker-compose.yml     # Container configuration
├── nginx.conf             # Nginx routing rules
├── index.html             # Legacy (not used)
├── js/                    # Legacy JavaScript
├── welding/index.html     # Welding simulator
├── main_site/             # Main portfolio site
├── floorplan/             # Floorplan app (properly served)
│   ├── index.html
│   └── js/app.js
└── backend/               # Node.js API
```

### Volume Mounts
The following are mounted into the nginx container:
- `./index.html` → `/usr/share/nginx/html/index.html`
- `./js` → `/usr/share/nginx/html/js`
- `./welding` → `/usr/share/nginx/html/welding`
- `./main_site` → `/usr/share/nginx/html/main_site`
- `./floorplan` → `/usr/share/nginx/html/floorplan`

## Common Commands

### Restart Nginx (after file changes)
```bash
ssh arner@46.62.216.163 "cd ~/task_app && docker-compose restart nginx"
```

### Restart All Services
```bash
ssh arner@46.62.216.163 "cd ~/task_app && docker-compose down && docker-compose up -d"
```

### View Logs
```bash
ssh arner@46.62.216.163 "cd ~/task_app && docker-compose logs -f"
```

### Prune Docker
```bash
ssh arner@46.62.216.163 "docker system prune -af && docker builder prune -af"
```

## Deployment Rules

### When Editing Files
1. **Main site**: Edit files in `~/task_app/main_site/`
2. **Welding app**: Edit `~/task_app/welding/index.html`
3. **Floorplan app**: Edit `~/task_app/floorplan/index.html` and `~/task_app/floorplan/js/app.js`

### After Making Changes
1. Changes to mounted files are usually instant
2. If changes don't appear, restart nginx: `docker-compose restart nginx`
3. Clear browser cache with hard refresh: `Ctrl+Shift+R`
4. Update cache-buster version in script tags if needed (e.g., `app.js?v=4`)

### Favicon
All domains use the main site favicon via absolute URL:
```html
<link rel="icon" href="https://arnereabel.com/static/images/favicon.ico">
```

## Nginx Routes

```nginx
location /              → /usr/share/nginx/html/main_site
location /welding/      → /usr/share/nginx/html/welding/
location /floorplan/    → /usr/share/nginx/html/floorplan/
location /floorplan/js/ → /usr/share/nginx/html/floorplan/js/
location /floorplan/api/→ proxy to backend:3001
```

**Trailing slash redirects**: `/welding` → `/welding/` and `/floorplan` → `/floorplan/`

## Backups

| Backup | Location | Date |
|--------|----------|------|
| `vps_backup_helsinki` | VPS: `~/vps_backup_helsinki/` | Dec 2025 |
| `vps_backup_helsinki_2` | VPS: `~/vps_backup_helsinki_2/` | 2026-01-01 |
| `vps_backup_helsinki_2.tar.gz` | Local: `c:\Users\arne_r\website_nerfies\` | 2026-01-01 |

### Create Backup
```bash
ssh arner@46.62.216.163 "cp -r ~/task_app ~/vps_backup_NAME"
```

### Download Backup
```bash
ssh arner@46.62.216.163 "cd ~ && tar -czvf backup.tar.gz FOLDER/"
scp arner@46.62.216.163:~/backup.tar.gz .
```
