package com.huzaifashahbaz.fragmentsapp;
import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;
import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.fragment.app.Fragment;
public class FragmentA extends Fragment {
    @Nullable
    @Override
    public View onCreateView(@NonNull LayoutInflater inflater, @Nullable ViewGroup container, @Nullable Bundle savedInstanceState)
    {
        View fragmentView=inflater.inflate(R.layout.fragment_a_layout,container,false);
        TextView framentTV=fragmentView.findViewById(R.id.main_message_a);
        if (getArguments()!=null)
        {
            String msg=getArguments().getString(MainActivity.MSG_KEY);
            framentTV.setText(msg);
        }
        return fragmentView;
    }
}