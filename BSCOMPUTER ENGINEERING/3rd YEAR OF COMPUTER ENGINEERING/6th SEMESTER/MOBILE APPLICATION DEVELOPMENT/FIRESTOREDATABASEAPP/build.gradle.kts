// Top-level build file where you can add configuration options common to all sub-projects/modules.
plugins {
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

}