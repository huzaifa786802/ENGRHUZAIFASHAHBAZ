package com.huzaifashahbaz.prayeralarmappintent;
import android.app.AlarmManager;
import android.app.PendingIntent;
import android.content.Context;
import android.content.Intent;
import android.os.Bundle;
import android.widget.Button;
import android.widget.TextView;
import android.widget.TimePicker;
import android.widget.Toast;
import androidx.appcompat.app.AppCompatActivity;
import java.util.Calendar;
public class MainActivity extends AppCompatActivity {
    private TimePicker timePicker;
    private Button buttonSetAlarm;
    private TextView textViewStatus;
    private AlarmManager alarmManager;
    private PendingIntent pendingIntent;
    @Override
    protected void onCreate(Bundle savedInstanceState)
    {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        timePicker=findViewById(R.id.timePicker);
        buttonSetAlarm=findViewById(R.id.buttonSetAlarm);
        textViewStatus=findViewById(R.id.textViewStatus);
        alarmManager=(AlarmManager) getSystemService(Context.ALARM_SERVICE);
        buttonSetAlarm.setOnClickListener(v -> setAlarm());
    }
    private void setAlarm()
    {
        int hour=timePicker.getCurrentHour();
        int minute=timePicker.getCurrentMinute();
        Calendar calendar=Calendar.getInstance();
        calendar.set(Calendar.HOUR_OF_DAY,hour);
        calendar.set(Calendar.MINUTE,minute);
        calendar.set(Calendar.SECOND,0);
        Intent intent=new Intent(this, AlarmReceiver.class);
        pendingIntent=pendingIntent.getBroadcast(this,0,intent,PendingIntent.FLAG_UPDATE_CURRENT);
        alarmManager.setExact(AlarmManager.RTC_WAKEUP,calendar.getTimeInMillis(),pendingIntent);
        String alarmTime=String.format("%02d:%02d",hour,minute);
        textViewStatus.setText("Alarm set for"+alarmTime);
        Toast.makeText(this, "Alarm set for", Toast.LENGTH_SHORT).show();
    }
}