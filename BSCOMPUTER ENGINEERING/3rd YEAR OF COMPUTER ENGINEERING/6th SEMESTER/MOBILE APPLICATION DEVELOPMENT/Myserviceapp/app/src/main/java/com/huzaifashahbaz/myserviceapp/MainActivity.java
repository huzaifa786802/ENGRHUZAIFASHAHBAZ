package com.huzaifashahbaz.myserviceapp;
import androidx.appcompat.app.AppCompatActivity;//AppcompatActivityclass
import android.content.Intent;//intentclass
import android.os.Bundle;//bundleclass
import android.view.View;//view class
public class MainActivity extends AppCompatActivity {
    Intent serviceIntent;//private memebers of myservices app
    @Override
    protected void onCreate(Bundle savedInstanceState) {//Oncreate function of bundle
        super.onCreate(savedInstanceState);//oncreate initializes
        setContentView(R.layout.activity_main);//content view of  activity_main and also main activity java file created
    }
    public void startService(View view){//startservice function of myservices
        serviceIntent = new Intent(getApplicationContext(), MyService.class);//serviceintent call by the myservices class
        startService(serviceIntent);
    }
    public void stopService(View view){//stopservice function of myservices
        serviceIntent = new Intent(getApplicationContext(), MyService.class);//serviceintent call by the myservices class
        stopService(serviceIntent);
    }
}