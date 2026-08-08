package com.huzaifashahbaz.prayeralarmsharedpreferences;
import android.app.AlarmManager;
import android.app.PendingIntent;
import android.content.Context;
import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.widget.Button;
import android.widget.TextView;
import android.widget.TimePicker;
import android.widget.Toast;
import androidx.appcompat.app.AppCompatActivity;
import java.util.Calendar;
public class MainActivity extends AppCompatActivity {
    private TimePicker timePicker;
    private Button setAlarmButton;
    private TextView prayerTimeTextView;
    private static final String PREFS_NAME = "PrayerAlarmPrefs";
    private static final String PREF_HOUR = "hour";
    private static final String PREF_MINUTE = "minute";
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        timePicker = findViewById(R.id.timePicker);
        setAlarmButton = findViewById(R.id.setAlarmButton);
        prayerTimeTextView = findViewById(R.id.prayerTimeTextView);
        SharedPreferences preferences = getSharedPreferences(PREFS_NAME, MODE_PRIVATE);
        int hour = preferences.getInt(PREF_HOUR, 0);
        int minute = preferences.getInt(PREF_MINUTE, 0);
        updatePrayerTimeTextView(hour, minute);
        setAlarmButton.setOnClickListener(v -> {
            int selectedHour = timePicker.getHour();
            int selectedMinute = timePicker.getMinute();
            setAlarm(selectedHour, selectedMinute);
            savePrayerTime(selectedHour, selectedMinute);
            updatePrayerTimeTextView(selectedHour, selectedMinute);
        });
    }
    private void setAlarm(int hour, int minute) {
        AlarmManager alarmManager = (AlarmManager) getSystemService(Context.ALARM_SERVICE);
        Intent intent = new Intent(this, AlarmReceiver.class);
        PendingIntent pendingIntent = PendingIntent.getBroadcast(this, 0, intent, 0);
        Calendar calendar = Calendar.getInstance();
        calendar.set(Calendar.HOUR_OF_DAY, hour);
        calendar.set(Calendar.MINUTE, minute);
        calendar.set(Calendar.SECOND, 0);
        alarmManager.setExact(AlarmManager.RTC_WAKEUP, calendar.getTimeInMillis(), pendingIntent);
        Toast.makeText(this, "Alarm set for " + hour + ":" + minute, Toast.LENGTH_SHORT).show();
    }
    private void savePrayerTime(int hour, int minute) {
        SharedPreferences.Editor editor = getSharedPreferences(PREFS_NAME, MODE_PRIVATE).edit();
        editor.putInt(PREF_HOUR, hour);
        editor.putInt(PREF_MINUTE, minute);
        editor.apply();
    }
    private void updatePrayerTimeTextView(int hour, int minute) {
        String timeText = "Prayer Time: " + String.format("%02d:%02d", hour, minute);
        prayerTimeTextView.setText(timeText);
    }
}