package com.huzaifashahbaz.notepadapp;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import androidx.appcompat.app.AppCompatActivity;
public class NewNoteActivity extends AppCompatActivity {
    private EditText editTextNote;
    private Note existingNote;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_new_note);
        editTextNote = findViewById(R.id.edittext_note);
        Button buttonSaveNote = findViewById(R.id.button_save_note);
        buttonSaveNote.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(NewNoteActivity.this, NewNoteActivity.class);
            }
        });
        existingNote = (Note) getIntent().getSerializableExtra("note");
        if (existingNote != null) {
            editTextNote.setText(existingNote.getContent());
        }
        buttonSaveNote.setOnClickListener(v -> {
            String noteContent = editTextNote.getText().toString();
            Note note = new Note(noteContent);
            Intent resultIntent = new Intent();
            resultIntent.putExtra("note", note);
            setResult(RESULT_OK, resultIntent);
            finish();
        });
    }
}