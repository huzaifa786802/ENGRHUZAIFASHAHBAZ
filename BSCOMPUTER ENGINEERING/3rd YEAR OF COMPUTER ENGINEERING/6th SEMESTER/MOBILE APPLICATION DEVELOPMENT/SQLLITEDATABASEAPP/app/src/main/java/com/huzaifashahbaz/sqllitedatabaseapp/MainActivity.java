package com.huzaifashahbaz.sqllitedatabaseapp;
import android.os.Bundle;
import android.view.View;
import android.widget.EditText;
import android.widget.ListView;
import android.widget.Toast;
import androidx.appcompat.app.AppCompatActivity;
import java.util.ArrayList;
public class MainActivity extends AppCompatActivity {
    EditText idET, nameET, addressET;
    SchoolDBHelper dbHelper;
    ListView listView;
    SchoolBaseAdapter adapter;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        idET = findViewById(R.id.id_et);
        nameET = findViewById(R.id.name_et);
        addressET = findViewById(R.id.add_et);
        listView = findViewById(R.id.list_view);
        dbHelper = new SchoolDBHelper(getApplicationContext());
        updateListView();
    }
    public void addNewEntry(View view) {
        if (!idET.getText().toString().matches("") &&
                !nameET.getText().toString().matches("") &&
                !addressET.getText().toString().matches("")) {
            int id = Integer.parseInt(idET.getText().toString());
            String name = nameET.getText().toString();
            String address = addressET.getText().toString();
            dbHelper.addEntry(id, name, address);
            updateListView();
        } else {
            Toast.makeText(this, "Fill all edit boxes", Toast.LENGTH_SHORT).show();
        }
    }
    void updateListView() {
        ArrayList<SchoolSetter> schoolSetters = dbHelper.readAll();
        adapter = new SchoolBaseAdapter(getApplicationContext(), schoolSetters);
        listView.setAdapter(adapter);
        listView.invalidateViews();
    }
}