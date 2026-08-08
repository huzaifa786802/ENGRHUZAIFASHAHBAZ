package com.huzaifashahbaz.androidbroadcastreceiverapp;
import android.content.Intent;
import android.content.IntentFilter;
import android.os.Bundle;
import android.view.View;
import androidx.appcompat.app.AppCompatActivity;
public class MainActivity extends AppCompatActivity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        MyReceiver receiver=new MyReceiver();
        IntentFilter filter1=new IntentFilter("android.intent.action.AIRPLANE_MODE");
        registerReceiver(receiver,filter1);
        IntentFilter filter2=new IntentFilter("com.example.mybroadcastreceiver.CUSTOM_INTENT");
        registerReceiver(receiver,filter2);
    }
    public void sendBR(View view)
    {
        Intent intent=new Intent("com.example.mybroadcastreceiver.CUSTOM_INTENT");
        sendBroadcast(intent);
    }
}