package com.huzaifashahbaz.androidserviceapp;
import androidx.appcompat.app.AppCompatActivity;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
public class MainActivity extends AppCompatActivity {
    Intent serviceIntent;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }
    public void startService(View view){
        serviceIntent = new Intent(getApplicationContext(), MyService.class);
        startService(serviceIntent);
    }
    public void stopService(View view){
        serviceIntent = new Intent(getApplicationContext(), MyService.class);
        stopService(serviceIntent);
    }
}