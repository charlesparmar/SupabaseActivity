# GitHub Actions Trigger Guide

This guide explains how to trigger the Add and Remove workflows from your phone.

## 🔗 Workflow URLs

### View Workflows in Browser:
- **Add Entry**: https://github.com/charlesparmar/SupabaseActivity/actions/workflows/add-entry.yml
- **Remove Entry**: https://github.com/charlesparmar/SupabaseActivity/actions/workflows/remove-entry.yml

### Manual Trigger (Browser):
1. Click on the workflow link above
2. Click the "Run workflow" button
3. Select the branch (main)
4. For Remove Entry: Enter the week number
5. Click "Run workflow"

## 📱 Trigger from Phone

To trigger workflows from your phone, you'll need a **GitHub Personal Access Token (PAT)**.

### Step 1: Create a Personal Access Token

1. Go to: https://github.com/settings/tokens
2. Click "Generate new token" → "Generate new token (classic)"
3. Give it a name: "Supabase Activity Actions"
4. Set expiration: Choose your preference
5. Select scopes:
   - ✅ `repo` (Full control of private repositories)
   - ✅ `workflow` (Update GitHub Action workflows)
6. Click "Generate token"
7. **Copy the token immediately** (you won't see it again!)

### Step 2: API Endpoints

#### Add Entry Workflow
```
POST https://api.github.com/repos/charlesparmar/SupabaseActivity/actions/workflows/add-entry.yml/dispatches
```

**Headers:**
```
Authorization: Bearer YOUR_GITHUB_TOKEN
Accept: application/vnd.github+json
X-GitHub-Api-Version: 2022-11-28
```

**Body:**
```json
{
  "ref": "main"
}
```

#### Remove Entry Workflow
```
POST https://api.github.com/repos/charlesparmar/SupabaseActivity/actions/workflows/remove-entry.yml/dispatches
```

**Headers:**
```
Authorization: Bearer YOUR_GITHUB_TOKEN
Accept: application/vnd.github+json
X-GitHub-Api-Version: 2022-11-28
```

**Body:**
```json
{
  "ref": "main",
  "inputs": {
    "week_number": "1"
  }
}
```

## 📲 Recommended Apps to Trigger from Phone

### Option 1: Shortcuts App (iOS)
Create shortcuts with HTTP requests to trigger the workflows.

**Add Entry Shortcut:**
1. Open Shortcuts app
2. Create new shortcut
3. Add "Get Contents of URL" action
4. Configure:
   - URL: `https://api.github.com/repos/charlesparmar/SupabaseActivity/actions/workflows/add-entry.yml/dispatches`
   - Method: POST
   - Headers:
     - `Authorization`: `Bearer YOUR_TOKEN`
     - `Accept`: `application/vnd.github+json`
   - Request Body: JSON
     ```json
     {"ref": "main"}
     ```

### Option 2: HTTP Shortcuts App (Android)
1. Install "HTTP Shortcuts" or "HTTP Request Shortcuts"
2. Create new shortcut
3. Configure the same API details as above

### Option 3: Workflow App (iOS/Android)
1. Install "Workflow" or "GitHub Actions" app
2. Authenticate with GitHub
3. Select your repository
4. Trigger workflows directly

### Option 4: Pushcut (iOS) with API
1. Install Pushcut app
2. Create a new notification
3. Add an action with the API request
4. Trigger via notification

### Option 5: Tasker (Android)
1. Install Tasker
2. Create new task
3. Add HTTP Post action
4. Configure with the API details above

### Option 6: curl Command (Any device with terminal)

**Add Entry:**
```bash
curl -X POST \
  -H "Authorization: Bearer YOUR_GITHUB_TOKEN" \
  -H "Accept: application/vnd.github+json" \
  -H "X-GitHub-Api-Version: 2022-11-28" \
  https://api.github.com/repos/charlesparmar/SupabaseActivity/actions/workflows/add-entry.yml/dispatches \
  -d '{"ref":"main"}'
```

**Remove Entry (week number 1):**
```bash
curl -X POST \
  -H "Authorization: Bearer YOUR_GITHUB_TOKEN" \
  -H "Accept: application/vnd.github+json" \
  -H "X-GitHub-Api-Version: 2022-11-28" \
  https://api.github.com/repos/charlesparmar/SupabaseActivity/actions/workflows/remove-entry.yml/dispatches \
  -d '{"ref":"main","inputs":{"week_number":"1"}}'
```

## 🔐 Security Notes

- ⚠️ **Keep your Personal Access Token secure!**
- Don't share your token publicly
- Use token expiration for added security
- Revoke tokens you're not using
- Consider using fine-grained tokens for better security

## 📊 Monitoring Workflow Runs

After triggering a workflow, you can monitor its status:
- **Actions Tab**: https://github.com/charlesparmar/SupabaseActivity/actions
- You'll receive push notifications via Pushover when the scripts complete

## 🎯 Quick Links

| Action | Browser Trigger | API Endpoint |
|--------|----------------|--------------|
| **Add Entry** | [Run Workflow](https://github.com/charlesparmar/SupabaseActivity/actions/workflows/add-entry.yml) | `POST .../add-entry.yml/dispatches` |
| **Remove Entry** | [Run Workflow](https://github.com/charlesparmar/SupabaseActivity/actions/workflows/remove-entry.yml) | `POST .../remove-entry.yml/dispatches` |
| **View All Runs** | [Actions Tab](https://github.com/charlesparmar/SupabaseActivity/actions) | - |

## 💡 Tips

1. **Add to Home Screen**: On iOS, you can add Shortcuts to your home screen for one-tap access
2. **Widget Support**: iOS Shortcuts can be added as widgets for quick access
3. **Voice Commands**: Both iOS and Android support voice-triggered shortcuts
4. **Automation**: Set up scheduled triggers or location-based automation
5. **Check Status**: Always verify the workflow ran successfully in the Actions tab

