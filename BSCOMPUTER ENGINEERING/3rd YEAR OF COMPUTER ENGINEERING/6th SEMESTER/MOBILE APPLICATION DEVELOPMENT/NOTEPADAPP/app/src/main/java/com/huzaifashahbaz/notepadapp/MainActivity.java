package com.huzaifashahbaz.notepadapp;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.ListView;
import android.widget.TextView;
import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;
import java.util.ArrayList;
public class MainActivity extends AppCompatActivity {
    private static final int REQUEST_CODE_NEW_NOTE = 1;
    private ArrayList<Note> notes;
    private ArrayAdapter<Note> adapter;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        notes = new ArrayList<>();
        ListView listViewNotes = findViewById(R.id.listview_notes);
        adapter = new ArrayAdapter<Note>(this, android.R.layout.simple_list_item_2, android.R.id.text1, notes) {
            @Override
            public View getView(int position, View convertView, ViewGroup parent) {
                View view = super.getView(position, convertView, parent);
                TextView text1 = view.findViewById(android.R.id.text1);
                TextView text2 = view.findViewById(android.R.id.text2);
                Note note = getItem(position);
                if (note != null) {
                    text1.setText(note.getContent());
                    text2.setText(note.getDateTime());
                }
                return view;
            }
        };
        listViewNotes.setAdapter(adapter);
        Button buttonNewNote = findViewById(R.id.button_new_note);
        buttonNewNote.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(MainActivity.this, NewNoteActivity.class);
                startActivityForResult(intent, REQUEST_CODE_NEW_NOTE);
            }
        });
        listViewNotes.setOnItemClickListener((parent, view, position, id) -> {
            Note note = notes.get(position);
            Intent intent = new Intent(MainActivity.this, NewNoteActivity.class);
            intent.putExtra("note", note);
            startActivityForResult(intent, REQUEST_CODE_NEW_NOTE);
        });
    }
    @Override
    protected void onActivityResult(int requestCode, int resultCode, @Nullable Intent data) {
        super.onActivityResult(requestCode, resultCode, data);
        if (requestCode == REQUEST_CODE_NEW_NOTE && resultCode == RESULT_OK) {
            Note note = (Note) data.getSerializableExtra("note");
            if (note != null) {
                notes.add(note);
                adapter.notifyDataSetChanged();
            }
        }
    }
}