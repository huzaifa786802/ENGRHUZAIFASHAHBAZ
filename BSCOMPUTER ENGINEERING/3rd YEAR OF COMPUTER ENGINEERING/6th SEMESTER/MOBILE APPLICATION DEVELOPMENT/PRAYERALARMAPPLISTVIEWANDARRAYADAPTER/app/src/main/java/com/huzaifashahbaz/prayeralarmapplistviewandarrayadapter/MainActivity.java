package com.huzaifashahbaz.prayeralarmapplistviewandarrayadapter;
import android.app.AlarmManager;
import android.app.PendingIntent;
import android.content.Context;
import android.content.Intent;
import android.os.Bundle;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.ListView;
import android.widget.TextView;
import android.widget.Toast;
import androidx.appcompat.app.AppCompatActivity;
import java.util.Calendar;
public class MainActivity extends AppCompatActivity {
    private ListView listViewPrayers;
    private Button buttonSetAlarm;
    private TextView textViewStatus;
    private AlarmManager alarmManager;
    private PendingIntent pendingIntent;
    private String selectedTime;
    private String[] prayerTimes = {"3:20", "12:05", "5:03", "7:11", "8:52"};
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        listViewPrayers = findViewById(R.id.listViewPrayers);
        buttonSetAlarm = findViewById(R.id.buttonSetAlarm);
        alarmManager = (AlarmManager) getSystemService(Context.ALARM_SERVICE);
        ArrayAdapter<String> adapter = new ArrayAdapter<>(this, android.R.layout.simple_list_item_single_choice, prayerTimes);
        listViewPrayers.setAdapter(adapter);
        listViewPrayers.setChoiceMode(ListView.CHOICE_MODE_SINGLE);
        listViewPrayers.setOnItemClickListener((parent, view, position, id) -> selectedTime = prayerTimes[position]);
        buttonSetAlarm.setOnClickListener(v -> setAlarm());
    }
    private void setAlarm() {
        if (selectedTime == null) {
            Toast.makeText(this, "Please select a prayer time", Toast.LENGTH_SHORT).show();
            return;
        }
        String[] timeParts = selectedTime.split(":");
        int hour = Integer.parseInt(timeParts[0]);
        int minute = Integer.parseInt(timeParts[1]);
        Calendar calendar = Calendar.getInstance();
        calendar.set(Calendar.HOUR_OF_DAY, hour);
        calendar.set(Calendar.MINUTE, minute);
        calendar.set(Calendar.SECOND, 0);
        Intent intent = new Intent(this, AlarmReceiver.class);
        pendingIntent = PendingIntent.getBroadcast(this, 0, intent, PendingIntent.FLAG_UPDATE_CURRENT);
        alarmManager.setExact(AlarmManager.RTC_WAKEUP, calendar.getTimeInMillis(), pendingIntent);
        textViewStatus.setText("Alarm set for " + selectedTime);
        Toast.makeText(this, "Alarm set for " + selectedTime, Toast.LENGTH_SHORT).show();
    }
}