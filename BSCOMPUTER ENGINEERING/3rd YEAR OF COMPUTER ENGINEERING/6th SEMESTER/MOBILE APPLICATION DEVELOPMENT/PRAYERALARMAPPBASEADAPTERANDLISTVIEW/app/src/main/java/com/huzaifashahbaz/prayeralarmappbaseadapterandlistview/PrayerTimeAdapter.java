package com.huzaifashahbaz.prayeralarmappbaseadapterandlistview;
import android.content.Context;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.BaseAdapter;
import android.widget.RadioButton;
import android.widget.TextView;
public class PrayerTimeAdapter extends BaseAdapter {
    private Context context;
    private String[] prayerTimes;
    private int selectedPosition = -1;
    public PrayerTimeAdapter(Context context, String[] prayerTimes) {
        this.context = context;
        this.prayerTimes = prayerTimes;
    }
    @Override
    public int getCount() {
        return prayerTimes.length;
    }
    @Override
    public Object getItem(int position) {
        return prayerTimes[position];
    }
    @Override
    public long getItemId(int position) {
        return position;
    }
    @Override
    public View getView(int position, View convertView, ViewGroup parent) {
        ViewHolder holder;
        if (convertView == null) {
            convertView = LayoutInflater.from(context).inflate(R.layout.activity_prayer_time_item, parent, false);
            holder = new ViewHolder();
            holder.textViewTime = convertView.findViewById(R.id.textViewTime);
            holder.radioButton = convertView.findViewById(R.id.radioButton);
            convertView.setTag(holder);
        } else {
            holder = (ViewHolder) convertView.getTag();
        }
        holder.textViewTime.setText(prayerTimes[position]);
        holder.radioButton.setChecked(position == selectedPosition);
        convertView.setOnClickListener(v -> {
            selectedPosition = position;
            notifyDataSetChanged();
        });
        return convertView;
    }
    public String getSelectedTime() {
        if (selectedPosition != -1) {
            return prayerTimes[selectedPosition];
        }
        return null;
    }

    private static class ViewHolder {
        TextView textViewTime;
        RadioButton radioButton;
    }
}