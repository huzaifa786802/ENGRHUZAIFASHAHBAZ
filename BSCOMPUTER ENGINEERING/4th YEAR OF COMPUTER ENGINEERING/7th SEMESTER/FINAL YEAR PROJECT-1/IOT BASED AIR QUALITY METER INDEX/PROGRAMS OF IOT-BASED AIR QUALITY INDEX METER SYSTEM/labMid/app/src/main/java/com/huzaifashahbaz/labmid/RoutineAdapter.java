package com.huzaifashahbaz.labmid;

import android.content.Context;
import android.graphics.Color;
import android.view.*;
import android.widget.*;

import java.util.List;

public class RoutineAdapter extends ArrayAdapter<Routine> {
    public RoutineAdapter(Context context, List<Routine> routines) {
        super(context, 0, routines);
    }

    @Override
    public View getView(int position, View convertView, ViewGroup parent) {
        Routine routine = getItem(position);
        if (convertView == null) {
            convertView = LayoutInflater.from(getContext()).inflate(R.layout.routine_item, parent, false);
        }

        TextView title = convertView.findViewById(R.id.textTitle);
        ImageView star = convertView.findViewById(R.id.imageStar);
        LinearLayout layout = convertView.findViewById(R.id.itemLayout);

        title.setText(routine.getName());

        if ("Urgent".equalsIgnoreCase(routine.getUrgency())) {
            layout.setBackgroundColor(Color.RED);
        } else {
            layout.setBackgroundColor(Color.TRANSPARENT);
        }

        if (routine.getRating() == 5) {
            star.setVisibility(View.VISIBLE);
        } else {
            star.setVisibility(View.GONE);
        }

        return convertView;
    }
}
