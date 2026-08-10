# 🚀 Quick Login Guide - HeartCheck DL

## ✅ The login page is NOW WORKING!

**Server Status**: ✅ Running at `http://localhost:5000`

---

## 🎯 Quick Start (30 seconds)

### Step 1: Open Your Browser
Navigate to:
```
http://localhost:5000/login
```

### Step 2: Login with Admin Account
```
Username: admin
Password: admin123
```

### Step 3: Click "Sign In"
You'll be redirected to the admin dashboard! 🎉

---

## 🆕 Create Your Own Account

### Step 1: Click "Create one now"
Or go directly to:
```
http://localhost:5000/register
```

### Step 2: Fill in the Form
- **Username**: Choose a unique username
- **Email**: Your email address
- **Password**: At least 6 characters
- **Confirm Password**: Must match
- **Full Name**: Your full name
- **Age**: (Optional) Your age

### Step 3: Submit
You'll be automatically logged in! 🎊

---

## 🎨 What You'll See

### Login Page Features
- 🌟 Beautiful animated card
- ❤️ Heart logo with gradient
- 🔒 Secure password input
- ⚡ Smooth animations
- 💬 Flash messages for feedback
- 🏠 "Back to Home" button

### After Login
- 👤 Your name in navigation
- 📊 Access to all features
- 📝 Prediction history
- 🔓 Logout option

---

## 🔐 All Available Accounts

### 1. Admin Account (Default)
```
Username: admin
Password: admin123
Access: Full admin panel
```

### 2. Your Custom Account
Create at: http://localhost:5000/register

---

## 🧪 Test the Login Right Now!

### Method 1: Web Browser
1. Open: http://localhost:5000/login
2. Enter: `admin` / `admin123`
3. Click "Sign In"

### Method 2: Command Line Test
```powershell
# Test GET request (should return 200)
Invoke-WebRequest -Uri "http://localhost:5000/login" -Method GET

# Test POST login (should redirect to home)
$body = @{
    username = "admin"
    password = "admin123"
}
Invoke-WebRequest -Uri "http://localhost:5000/login" -Method POST -Body $body -SessionVariable session
```

---

## 📱 Available Pages After Login

| Page | URL | Description |
|------|-----|-------------|
| 🏠 Home | `/` | Landing page with overview |
| 📊 Predict | `/predict` | Heart risk assessment form |
| 📈 Results | `/results` | View prediction results |
| 📉 Dataset | `/dataset` | Dataset insights & visualizations |
| ℹ️ About | `/about` | Project information |
| 👤 Admin | `/admin` | Admin panel (admin only) |
| 🔓 Logout | `/logout` | Sign out |

---

## ⚡ Common Tasks

### Make a Prediction
1. Login → Go to http://localhost:5000/predict
2. Fill in all health parameters
3. Click "Analyze My Heart Risk"
4. View your personalized results
5. Results automatically saved to your account

### View Your History (Admin Only)
1. Login as admin
2. Go to http://localhost:5000/admin
3. See all predictions from all users
4. View user statistics

### Change Password (Future Feature)
Currently not implemented. To reset:
1. Contact admin
2. Or delete user from database and re-register

---

## 🛠️ Troubleshooting

### "Page not loading"
**Check server is running:**
```powershell
# Should show "Running on http://127.0.0.1:5000"
# Look for the Flask server terminal
```

**Restart if needed:**
```powershell
# Stop server (Ctrl+C in server terminal)
# Restart:
cd c:\Users\manii\Documents\HTML\HeartCheckDL
.\venv\Scripts\Activate.ps1
$env:FLASK_APP="api/app.py"
flask run --host=0.0.0.0 --port=5000
```

### "Invalid username or password"
- ✅ Check you typed correctly
- ✅ Admin credentials: `admin` / `admin123`
- ✅ Make sure caps lock is OFF
- ✅ No spaces before/after username

### "Database error"
```powershell
# Re-initialize database
cd c:\Users\manii\Documents\HTML\HeartCheckDL
.\venv\Scripts\Activate.ps1
python -c "from api.app import init_db; init_db()"
```

### Session expires immediately
- Clear browser cookies for localhost:5000
- Try incognito/private mode
- Restart Flask server

---

## 🎉 Success Indicators

You know it's working when you see:
- ✅ Login page loads with heart logo
- ✅ Can type in username and password fields
- ✅ "Sign In" button is clickable
- ✅ After login, you see "Welcome back, [Name]!" message
- ✅ Navigation shows your username
- ✅ Can access predict and other pages
- ✅ Can logout successfully

---

## 📸 What to Expect

### Login Page
```
┌─────────────────────────────────┐
│     [Back to Home]              │
│                                 │
│       ❤️ [Heart Logo]            │
│                                 │
│     Welcome Back                │
│  Sign in to access your         │
│  heart health dashboard         │
│                                 │
│  Username: [_______________]    │
│  Password: [_______________]    │
│                                 │
│     [    Sign In    ]           │
│                                 │
│  Don't have an account?         │
│     Create one now              │
└─────────────────────────────────┘
```

### After Successful Login
```
Flash Message: "Welcome back, Administrator!" (green)
Redirected to: Home Page or Admin Panel
Navigation: Shows "admin" with logout option
```

---

## 💡 Pro Tips

1. **Bookmark the login page**: `http://localhost:5000/login`
2. **Use admin for testing**: Full access to all features
3. **Create test accounts**: Test the user experience
4. **Check predictions**: All saved predictions are in admin panel
5. **Session persists**: No need to re-login if server stays running

---

## 🎊 You're All Set!

**The login system is fully functional and ready to use!**

**Next Steps:**
1. Open http://localhost:5000/login
2. Login with `admin` / `admin123`
3. Explore the application
4. Make predictions
5. View results and history

---

## 📞 Need Help?

### Check Server Logs
Look at the Flask server terminal for error messages

### Verify Database
```powershell
python -c "import sqlite3; conn = sqlite3.connect('db/predictions.sqlite'); cursor = conn.cursor(); cursor.execute('SELECT COUNT(*) FROM users'); print(f'Users: {cursor.fetchone()[0]}'); conn.close()"
```

### Test Pages
- Home: http://localhost:5000/
- Login: http://localhost:5000/login
- Register: http://localhost:5000/register
- Predict: http://localhost:5000/predict (requires login)

---

## 🔥 Go ahead and login now!

Open your browser and visit: **http://localhost:5000/login**

Use credentials: **admin** / **admin123**

Enjoy your HeartCheck DL application! ❤️
