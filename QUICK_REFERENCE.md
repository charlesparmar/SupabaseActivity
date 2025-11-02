# 📱 Quick Reference - Trigger from Phone

## 🔗 Direct Workflow URLs (Tap to Trigger in Browser)

### Add Entry
**Browser URL:** 
```
https://github.com/charlesparmar/SupabaseActivity/actions/workflows/add-entry.yml
```
👆 Click "Run workflow" button, select "main" branch, then click "Run workflow"

### Remove Entry  
**Browser URL:**
```
https://github.com/charlesparmar/SupabaseActivity/actions/workflows/remove-entry.yml
```
👆 Click "Run workflow" button, enter week number, then click "Run workflow"

---

## 🚀 API Endpoints (For Apps & Shortcuts)

### Add Entry API
```
POST https://api.github.com/repos/charlesparmar/SupabaseActivity/actions/workflows/add-entry.yml/dispatches
```

**Minimal curl command:**
```bash
curl -X POST \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Accept: application/vnd.github+json" \
  https://api.github.com/repos/charlesparmar/SupabaseActivity/actions/workflows/add-entry.yml/dispatches \
  -d '{"ref":"main"}'
```

### Remove Entry API (Week 1 example)
```
POST https://api.github.com/repos/charlesparmar/SupabaseActivity/actions/workflows/remove-entry.yml/dispatches
```

**Minimal curl command:**
```bash
curl -X POST \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Accept: application/vnd.github+json" \
  https://api.github.com/repos/charlesparmar/SupabaseActivity/actions/workflows/remove-entry.yml/dispatches \
  -d '{"ref":"main","inputs":{"week_number":"1"}}'
```

---

## 🔑 Get Your GitHub Token

1. Go to: https://github.com/settings/tokens
2. Click "Generate new token (classic)"
3. Enable: `repo` and `workflow` scopes
4. Copy the token (you won't see it again!)

---

## 📊 Monitor Runs

**Actions Dashboard:**
```
https://github.com/charlesparmar/SupabaseActivity/actions
```

---

## 🎯 Best Apps for Phone Triggering

### iOS:
- **Shortcuts** (Built-in, free) ⭐ Recommended
- **Pushcut** (Notifications with actions)
- **Workflow** (GitHub Actions app)

### Android:
- **HTTP Shortcuts** (Free) ⭐ Recommended  
- **Tasker** (Powerful automation)
- **HTTP Request Shortcuts**

### Both:
- **GitHub Mobile App** → Actions tab → Manually trigger

---

## 💾 Save These URLs

| Purpose | URL |
|---------|-----|
| Add Entry | https://github.com/charlesparmar/SupabaseActivity/actions/workflows/add-entry.yml |
| Remove Entry | https://github.com/charlesparmar/SupabaseActivity/actions/workflows/remove-entry.yml |
| All Actions | https://github.com/charlesparmar/SupabaseActivity/actions |
| Get Token | https://github.com/settings/tokens |
| Full Guide | https://github.com/charlesparmar/SupabaseActivity/blob/main/GITHUB_ACTIONS_GUIDE.md |

---

## ⚡ Quick Setup Checklist

- ✅ GitHub Secrets configured (you mentioned you've done this!)
- ⚡ Create Personal Access Token
- ⚡ Set up Shortcuts app (iOS) or HTTP Shortcuts (Android)
- ⚡ Add shortcuts to home screen
- ⚡ Test by triggering a workflow
- ⚡ Check Actions tab for results
- ⚡ Receive Pushover notification!

---

**Need more details?** Check [GITHUB_ACTIONS_GUIDE.md](GITHUB_ACTIONS_GUIDE.md) for complete setup instructions!

