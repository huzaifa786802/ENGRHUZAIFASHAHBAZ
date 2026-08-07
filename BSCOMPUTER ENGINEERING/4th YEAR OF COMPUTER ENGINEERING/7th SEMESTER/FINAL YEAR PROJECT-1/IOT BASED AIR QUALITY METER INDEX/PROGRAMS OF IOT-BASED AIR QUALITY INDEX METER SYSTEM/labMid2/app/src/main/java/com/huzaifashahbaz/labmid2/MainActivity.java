package com.huzaifashahbaz.labmid2;

import android.os.Bundle;
import android.view.View;
import android.widget.*;
import androidx.appcompat.app.AppCompatActivity;
import java.util.ArrayList;

public class MainActivity extends AppCompatActivity {

    private EditText memberNameEditText;
    private Spinner teamRoleSpinner;
    private RadioGroup experienceGroup;
    private Button submitButton;
    private ListView memberListView;

    private ArrayList<Member> memberList;
    private MemberAdapter memberAdapter;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        memberNameEditText = findViewById(R.id.member_name);
        teamRoleSpinner = findViewById(R.id.team_role);
        experienceGroup = findViewById(R.id.experience_group);
        submitButton = findViewById(R.id.submit_button);
        memberListView = findViewById(R.id.member_list_view);

        memberList = new ArrayList<>();
        memberAdapter = new MemberAdapter(this, memberList);
        memberListView.setAdapter(memberAdapter);

        submitButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                String name = memberNameEditText.getText().toString();
                String role = teamRoleSpinner.getSelectedItem().toString();
                int selectedId = experienceGroup.getCheckedRadioButtonId();

                if (name.isEmpty() || selectedId == -1) {
                    Toast.makeText(MainActivity.this, "Please fill all fields", Toast.LENGTH_SHORT).show();
                    return;
                }

                if (memberList.size() >= 5) {
                    Toast.makeText(MainActivity.this, "Maximum 5 members allowed", Toast.LENGTH_SHORT).show();
                    return;
                }

                RadioButton selectedButton = findViewById(selectedId);
                String experience = selectedButton.getText().toString();

                Member newMember = new Member(name, role, experience);
                memberList.add(newMember);
                memberAdapter.notifyDataSetChanged();
            }
        });
    }
}
