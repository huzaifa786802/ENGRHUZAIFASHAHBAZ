package com.huzaifashahbaz.myserviceapp;//package name where is the app working and function
import android.app.Service;//app service class
import android.content.Intent;//intent class
import android.os.IBinder;//IBinder class
import android.util.Log;//log class
import androidx.annotation.Nullable;//Nullable class
public class MyService extends Service {
    @Nullable
    @Override
    public IBinder onBind(Intent intent) {
        return null;
    }//IBinder function called
    @Override
    public int onStartCommand(Intent intent, int flags, int startId) {//OnstartCommand function called
        serviceThread thread = new serviceThread(startId);//servicetherad from onstart command
        thread.start();
        return START_STICKY;
    }
    @Override
    public void onDestroy() {//on destroy function
        super.onDestroy();
        Log.d("MyService", "onStartCommand: Service Stopped");
    }
    class serviceThread extends Thread {//service therad class
        int threadID;
        serviceThread(int threadID) {
            this.threadID = threadID;
        }
        @Override
        public void run() {//run fucntion called
            try {
                for (int i = 0; i < 10; i++) {//for loop declares in run function
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