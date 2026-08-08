package com.huzaifashahbaz.androidserviceapp;
import android.app.Service;
import android.content.Intent;
import android.os.IBinder;
import android.util.Log;
import androidx.annotation.Nullable;
public class MyService extends Service {
    @Nullable
    @Override
    public IBinder onBind(Intent intent) {
        return null;
    }
    @Override
    public int onStartCommand(Intent intent, int flags, int startId) {
        serviceThread thread = new serviceThread(startId);
        thread.start();
        return START_STICKY;
    }
    @Override
    public void onDestroy() {
        super.onDestroy();
        Log.d("MyService", "onStartCommand: Service Stopped");
    }
    class serviceThread extends Thread {
        int threadID;
        serviceThread(int threadID) {
            this.threadID = threadID;
        }
        @Override
        public void run() {
            try {
                for (int i = 0; i < 10; i++) {
                    Log.d("MyService", "serviceRunnable Running i = " + i);
                    Thread.sleep(1000);
                }
            } catch (Exception e) {
                Log.d("MyService", "serviceRunnable Error " + e);
            }
            stopSelf(threadID);
        }
    }
}