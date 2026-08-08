plugins {
    alias(libs.plugins.android.application)
}

android {
    namespace = "com.huzaifashahbaz.firestoredatabaseapp"
    compileSdk = 34

    defaultConfig {
        applicationId = "com.huzaifashahbaz.firestoredatabaseapp"
        minSdk = 34
        targetSdk = 34
        versionCode = 1
        versionName = "1.0"

        testInstrumentationRunner = "androidx.test.runner.AndroidJUnitRunner"
    }

    buildTypes {
        release {
            isMinifyEnabled = false
            proguardFiles(getDefaultProguardFile("proguard-android-optimize.txt"), "proguard-rules.pro")
        }
    }
    compileOptions {
        sourceCompatibility = JavaVersion.VERSION_1_8
        targetCompatibility = JavaVersion.VERSION_1_8
    }
}

dependencies {

    implementation(libs.appcompat)
    implementation(libs.material)
    implementation(libs.activity)
    implementation(libs.constraintlayout)
    testImplementation(libs.junit)
    androidTestImplementation(libs.ext.junit)
    androidTestImplementation(libs.espresso.core)
}
plugins {
    id 'com.android.application'
    id 'com.google.gms.google-services'
}

android {
    // ...
}

dependencies {
    implementation 'com.google.firebase:firebase-firestore:24.2.0'
    implementation 'com.google.firebase:firebase-analytics:21.2.0'
    // Other dependencies
}
buildscript {
    repositories {
        // ...
        google()
    }
    dependencies {
        // ...
        classpath 'com.google.gms:google-services:4.3.10'
    }
}

allprojects {
    repositories {
        // ...
        google()
    }
}
