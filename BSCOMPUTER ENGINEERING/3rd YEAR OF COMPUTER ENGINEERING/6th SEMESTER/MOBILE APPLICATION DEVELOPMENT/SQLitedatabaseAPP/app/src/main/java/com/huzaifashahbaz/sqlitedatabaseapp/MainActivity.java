package com.huzaifashahbaz.sqlitedatabaseapp;
import android.database.Cursor;
import android.os.Bundle;
import android.view.View;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ListView;
import android.widget.Toast;
import androidx.appcompat.app.AlertDialog;
import androidx.appcompat.app.AppCompatActivity;
import java.util.ArrayList;
public class MainActivity extends AppCompatActivity {
    Button btnAddData, btnViewAll;
    DatabaseHelper myDb;
    EditText editName, editRegNumber, editParentPhone, editAddress;
    ListView listView;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        myDb = new DatabaseHelper(this);
        editName = findViewById(R.id.editTextName);
        editRegNumber = findViewById(R.id.editTextRegNumber);
        editParentPhone = findViewById(R.id.editTextParentPhone);
        editAddress = findViewById(R.id.editTextAddress);
        listView = findViewById(R.id.listview);
        btnAddData = findViewById(R.id.button_add);
        btnViewAll = findViewById(R.id.button_view_all);
        btnAddData.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                addData();
            }
        });
        btnViewAll.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                viewAll();
            }
        });
    }
    public void addData() {
        boolean isInserted = myDb.insertData(
                editRegNumber.getText().toString(),
                editName.getText().toString(),
                editParentPhone.getText().toString(),
                editAddress.getText().toString()
        );
        if (isInserted) {
            Toast.makeText(MainActivity.this, "Data Inserted", Toast.LENGTH_LONG).show();
        } else {
            Toast.makeText(MainActivity.this, "Data not inserted", Toast.LENGTH_LONG).show();
        }
    }
    public void viewAll() {
        Cursor res = myDb.searchByNme(editName.getText().toString());
        if (res.getCount() == 0) {
            showMessage("Error", "Nothing found");
            return;
        }
        ArrayList<String> list = new ArrayList<>();
        while (res.moveToNext()) {
            list.add("Registration Number: " + res.getString(0) + "\n" +
                    "Name: " + res.getString(1) + "\n" +
                    "Parent Phone: " + res.getString(2) + "\n" +
                    "Address: " + res.getString(3));
        }
        ArrayAdapter<String> adapter = new ArrayAdapter<>(this, android.R.layout.simple_list_item_1, list);
        listView.setAdapter(adapter);
    }
    public void showMessage(String title, String message) {
        AlertDialog.Builder builder = new AlertDialog.Builder(this);
        builder.setCancelable(true);
        builder.setTitle(title);
        builder.setMessage(message);
        builder.show();
    }
}