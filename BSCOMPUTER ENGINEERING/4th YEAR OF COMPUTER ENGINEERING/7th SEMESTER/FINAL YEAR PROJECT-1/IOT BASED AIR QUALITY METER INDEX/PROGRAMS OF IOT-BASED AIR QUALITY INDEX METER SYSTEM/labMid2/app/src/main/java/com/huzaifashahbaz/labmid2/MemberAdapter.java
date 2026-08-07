package com.huzaifashahbaz.labmid2;

import android.content.Context;
import android.graphics.Color;
import android.view.*;
import android.widget.BaseAdapter;
import android.widget.TextView;
import java.util.ArrayList;

public class MemberAdapter extends BaseAdapter {
    private Context context;
    private ArrayList<Member> members;

    public MemberAdapter(Context context, ArrayList<Member> members) {
        this.context = context;
        this.members = members;
    }

    @Override
    public int getCount() {
        return members.size();
    }

    @Override
    public Object getItem(int position) {
        return members.get(position);
    }

    @Override
    public long getItemId(int position) {
        return position;
    }

    @Override
    public View getView(int position, View view, ViewGroup parent) {
        if (view == null)
            view = LayoutInflater.from(context).inflate(R.layout.member_item, parent, false);

        Member member = members.get(position);

        TextView name = view.findViewById(R.id.member_name_display);
        TextView role = view.findViewById(R.id.team_role_display);
        TextView experience = view.findViewById(R.id.experience_display);

        name.setText(member.getName());
        role.setText(member.getRole());
        experience.setText(member.getExperience());

        // Highlight beginner members with pink
        if (member.getExperience().equals("Beginner")) {
            view.setBackgroundColor(Color.parseColor("#FFB6C1")); // Light pink
        } else {
            view.setBackgroundColor(Color.TRANSPARENT);
        }

        return view;
    }
}
