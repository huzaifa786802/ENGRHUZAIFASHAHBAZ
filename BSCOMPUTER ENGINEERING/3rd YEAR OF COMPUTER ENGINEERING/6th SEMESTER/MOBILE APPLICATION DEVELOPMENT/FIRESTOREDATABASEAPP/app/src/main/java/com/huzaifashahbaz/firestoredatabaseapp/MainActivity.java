package com.huzaifashahbaz.firestoredatabaseapp;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;
import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;
import com.google.firebase.firestore.DocumentReference;
import com.google.firebase.firestore.FirebaseFirestore;
import com.google.firebase.firestore.FirebaseFirestoreException;
import com.google.firebase.firestore.Transaction;
public class MainActivity extends AppCompatActivity {
    private EditText regNumberEditText, nameEditText, parentPhoneEditText, addressEditText;
    private Button saveButton;
    private FirebaseFirestore db;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        db = FirebaseFirestore.getInstance();
        regNumberEditText = findViewById(R.id.editTextRegNumber);
        nameEditText = findViewById(R.id.editTextName);
        parentPhoneEditText = findViewById(R.id.editTextParentPhone);
        addressEditText = findViewById(R.id.editTextAddress);
        saveButton = findViewById(R.id.buttonSave);
        saveButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                saveStudent();
            }
        });
    }
    private void saveStudent() {
        String regNumber = regNumberEditText.getText().toString();
        String name = nameEditText.getText().toString();
        String parentPhone = parentPhoneEditText.getText().toString();
        String address = addressEditText.getText().toString();
        if (regNumber.isEmpty() || name.isEmpty() || parentPhone.isEmpty() || address.isEmpty()) {
            Toast.makeText(this, "Please fill all fields", Toast.LENGTH_SHORT).show();
            return;
        }
        Student student = new Student(regNumber, name, parentPhone, address);
        db.collection("students").document(regNumber).set(student)
                .addOnSuccessListener(aVoid -> {
                    Toast.makeText(MainActivity.this, "Student saved successfully", Toast.LENGTH_SHORT).show();
                    clearFields();
                })
                .addOnFailureListener(e -> Toast.makeText(MainActivity.this, "Error saving student: " + e.getMessage(), Toast.LENGTH_SHORT).show());
    }
    private void clearFields() {
        regNumberEditText.setText("");
        nameEditText.setText("");
        parentPhoneEditText.setText("");
        addressEditText.setText("");
    }
}