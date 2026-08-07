// src/main/java/com/example/dailyroutineapp/MainActivity.java
package com.huzaifashahbaz.labmid;

import android.app.DatePickerDialog;
import android.content.Intent;
import android.os.Bundle;
import android.widget.*;
import androidx.appcompat.app.AppCompatActivity;

import java.util.*;

public class MainActivity extends AppCompatActivity {

    EditText editActivityName, editTimeEstimate;
    Spinner spinnerRoutineType;
    RadioGroup radioGroupUrgency;
    Button btnPickDate, btnSubmit;
    TextView textSelectedDate;
    CheckBox checkMorningTask;
    Switch switchReminder;
    RatingBar ratingPriority;
    ListView listViewGoals;

    ArrayList<Routine> routineList;
    RoutineAdapter adapter;
    Calendar selectedCalendar;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        initializeViews();

        routineList = new ArrayList<>();
        adapter = new RoutineAdapter(this, routineList);
        listViewGoals.setAdapter(adapter);

        btnPickDate.setOnClickListener(v -> showDatePicker());

        btnSubmit.setOnClickListener(v -> {
            if (validateForm()) {
                Routine routine = collectFormData();
                routineList.add(routine);
                adapter.notifyDataSetChanged();
                Toast.makeText(this, "Routine Added", Toast.LENGTH_SHORT).show();
                clearForm();
            }
        });

        listViewGoals.setOnItemClickListener((parent, view, position, id) -> {
            Routine selectedRoutine = routineList.get(position);
            Intent intent = new Intent(MainActivity.this, DetailActivity.class);
            intent.putExtra("routine", selectedRoutine);
            startActivity(intent);
        });
    }

    private void initializeViews() {
        editActivityName = findViewById(R.id.editActivityName);
        editTimeEstimate = findViewById(R.id.editTimeEstimate);
        spinnerRoutineType = findViewById(R.id.spinnerRoutineType);
        radioGroupUrgency = findViewById(R.id.radioGroupUrgency);
        btnPickDate = findViewById(R.id.btnPickDate);
        btnSubmit = findViewById(R.id.btnSubmit);
        textSelectedDate = findViewById(R.id.textSelectedDate);
        checkMorningTask = findViewById(R.id.checkMorningTask);
        switchReminder = findViewById(R.id.switchReminder);
        ratingPriority = findViewById(R.id.ratingPriority);
        listViewGoals = findViewById(R.id.listViewGoals);

        ArrayAdapter<String> spinnerAdapter = new ArrayAdapter<>(
                this,
                android.R.layout.simple_spinner_dropdown_item,
                new String[]{"Work", "Leisure", "Wellness"}
        );
        spinnerRoutineType.setAdapter(spinnerAdapter);
    }

    private void showDatePicker() {
        final Calendar c = Calendar.getInstance();
        int year = c.get(Calendar.YEAR);
        int month = c.get(Calendar.MONTH);
        int day = c.get(Calendar.DAY_OF_MONTH);

        new DatePickerDialog(this, (view, y, m, d) -> {
            selectedCalendar = Calendar.getInstance();
            selectedCalendar.set(y, m, d);
            textSelectedDate.setText(d + "/" + (m + 1) + "/" + y);
        }, year, month, day).show();
    }

    private boolean validateForm() {
        if (editActivityName.getText().toString().trim().isEmpty()) {
            editActivityName.setError("Enter activity name");
            return false;
        }

        if (editTimeEstimate.getText().toString().trim().isEmpty()) {
            editTimeEstimate.setError("Enter time estimate");
            return false;
        }

        if (radioGroupUrgency.getCheckedRadioButtonId() == -1) {
            Toast.makeText(this, "Select urgency", Toast.LENGTH_SHORT).show();
            return false;
        }

        if (textSelectedDate.getText().toString().equals("No Date Selected")) {
            Toast.makeText(this, "Pick a schedule date", Toast.LENGTH_SHORT).show();
            return false;
        }

        return true;
    }

    private Routine collectFormData() {
        String name = editActivityName.getText().toString().trim();
        String time = editTimeEstimate.getText().toString().trim();
        String type = spinnerRoutineType.getSelectedItem().toString();

        int selectedUrgencyId = radioGroupUrgency.getCheckedRadioButtonId();
        RadioButton selectedUrgencyBtn = findViewById(selectedUrgencyId);
        String urgency = selectedUrgencyBtn.getText().toString();

        String date = textSelectedDate.getText().toString();
        boolean isMorning = checkMorningTask.isChecked();
        boolean hasReminder = switchReminder.isChecked();
        int rating = (int) ratingPriority.getRating();

        return new Routine(name, time, type, urgency, date, isMorning, hasReminder, rating);
    }

    private void clearForm() {
        editActivityName.setText("");
        editTimeEstimate.setText("");
        radioGroupUrgency.clearCheck();
        checkMorningTask.setChecked(false);
        switchReminder.setChecked(false);
        ratingPriority.setRating(0);
        textSelectedDate.setText("No Date Selected");
    }
}
