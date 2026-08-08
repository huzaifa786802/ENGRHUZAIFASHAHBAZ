package com.huzaifashahbaz.firestorebasedapp;
import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.Toast;
import java.util.HashMap;
import java.util.Map;
public class MainActivity extends AppCompatActivity {
    private Button button;
    private FirebaseFirestore db;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        button = findViewById(R.id.button);
        db = FirebaseFirestore.getInstance();
        button.setOnClickListener(new View.OClickListener() {
            @Override
            public void onClick(View v) {
                addDataToFirestore();
            }
        });
    }
    private void addDataToFirestore() {
        // Create a new user with a name, age, and email
        Map<String, Object> user = new HashMap<>();
        user.put("name", "John Doe");
        user.put("age", 30);
        user.put("email", "johndoe@example.com");
       db.collection("users")
                .add(user)
                .addOnSuccessListener(new OnSuccessListener() {
                    @Override
                    public void onSuccess(Void aVoid) {
                        Toast.makeText(MainActivity.this, "Data added successfully", Toast.LENGTH_SHORT).show();
                    }
                })
                .addOnFailureListener(new OnFailureListener() {
                    @Override
                    public void onFailure(@NonNull Exception e) {
                        Toast.makeText(MainActivity.this, "Error adding data to Firestore", Toast.LENGTH_SHORT).show();
                    }
                });
    }
}