[app]

# (str) Title of your application
title = شبیه ساز FC 27 غیر رسمی

# (str) Package name
package.name = fc27unofficial

# (str) Package domain (needed for android/ios packaging)
package.domain = org.fc27unofficial

# (str) Source code where main.py lives
source.dir = .

# (list) Source files to include
source.include_exts = py,png,jpg,jpeg,kv,old

# (list) List of inclusions using pattern matching
source.include_patterns = assets/*,assets/**/*

# (str) Application version
version = 1.0

# (list) Application requirements
requirements = python3,kivy,requests,pyjnius

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (bool) Fullscreen mode
fullscreen = 0

# (str) Presplash of the application
# presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
# icon.filename = %(source.dir)s/data/icon.png

# (str) Supported Android API
android.api = 29

# (str) Minimum API supported
android.minapi = 21

# (str) Android NDK version
android.ndk = 25b

# (str) Android architecture to build for
android.archs = arm64-v8a,armeabi-v7a

# (list) Android permissions
android.permissions = INTERNET,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE

# Keep the app's external-storage behavior compatible with the code's
# /storage/emulated/0/ paths on Android versions that support legacy storage.
android.private_storage = False

# (bool) Indicate if the application should be built in debug mode
# android.debug = 1

[buildozer]

# (int) Log level (0 = error only, 1 = error+warning, 2 = info, 3 = debug)
log_level = 2

# (bool) Warn if running buildozer as root
warn_on_root = 1
