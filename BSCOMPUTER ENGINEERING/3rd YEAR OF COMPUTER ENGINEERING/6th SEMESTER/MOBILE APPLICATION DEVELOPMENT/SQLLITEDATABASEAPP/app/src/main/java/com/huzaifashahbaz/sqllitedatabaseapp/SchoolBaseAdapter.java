package com.huzaifashahbaz.sqllitedatabaseapp;
import android.content.Context;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.BaseAdapter;
import android.widget.TextView;
import java.util.ArrayList;
public class SchoolBaseAdapter extends BaseAdapter {
    ArrayList<SchoolSetter> setter;
    LayoutInflater inflater;
    public SchoolBaseAdapter(Context context, ArrayList<SchoolSetter> setter) {
        this.setter = setter;
        inflater = LayoutInflater.from(context);
    }
    @Override
    public int getCount() {
        return setter.size();
    }
    @Override
    public Object getItem(int position) {
        return setter.get(position);
    }
    @Override
    public long getItemId(int position) {
        return position;
    }
    @Override
    public View getView(int position, View convertView, ViewGroup parent) {
// get view of custom item layout
        convertView = inflater.inflate(R.layout.activity_list_item_sql, null);
        TextView id = convertView.findViewById(R.id.item_id);
        TextView name = convertView.findViewById(R.id.item_name);
        TextView address = convertView.findViewById(R.id.item_address);
        id.setText(String.valueOf(setter.get(position).getId()));
        name.setText(String.valueOf(setter.get(position).getName()));
        address.setText(String.valueOf(setter.get(position).getAddress()));
        return convertView;
    }
}