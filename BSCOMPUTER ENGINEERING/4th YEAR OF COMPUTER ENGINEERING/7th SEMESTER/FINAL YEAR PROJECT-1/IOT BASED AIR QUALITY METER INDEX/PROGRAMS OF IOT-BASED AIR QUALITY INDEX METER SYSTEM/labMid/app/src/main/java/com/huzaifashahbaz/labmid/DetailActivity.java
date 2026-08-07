package com.huzaifashahbaz.labmid;

import android.os.Bundle;
import android.widget.TextView;
import androidx.appcompat.app.AppCompatActivity;

public class DetailActivity extends AppCompatActivity {
    TextView detailName, detailType, detailTime, detailUrgency,
            detailDate, detailMorning, detailReminder, detailRating;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_detail);

        Routine routine = (Routine) getIntent().getSerializableExtra("routine");

        detailName = findViewById(R.id.detailName);
        detailType = findViewById(R.id.detailType);
        detailTime = findViewById(R.id.detailTime);
        detailUrgency = findViewById(R.id.detailUrgency);
        detailDate = findViewById(R.id.detailDate);
        detailMorning = findViewById(R.id.detailMorning);
        detailReminder = findViewById(R.id.detailReminder);
        detailRating = findViewById(R.id.detailRating);

        detailName.setText("Activity: " + routine.getName());
        detailType.setText("Type: " + routine.getType());
        detailTime.setText("Time Estimate: " + routine.getTimeEstimate() + " mins");
        detailUrgency.setText("Urgency: " + routine.getUrgency());
        detailDate.setText("Scheduled Date: " + routine.getDate());
        detailMorning.setText("Morning Task: " + (routine.isMorningTask() ? "Yes" : "No"));
        detailReminder.setText("Reminder: " + (routine.hasReminder() ? "On" : "Off"));
        detailRating.setText("Priority: " + routine.getRating() + " stars");
    }
}
