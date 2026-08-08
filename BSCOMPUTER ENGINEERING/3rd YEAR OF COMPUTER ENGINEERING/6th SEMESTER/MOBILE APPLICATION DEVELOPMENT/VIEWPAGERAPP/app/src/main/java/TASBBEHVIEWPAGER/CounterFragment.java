package TASBBEHVIEWPAGER;
import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.TextView;
import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.fragment.app.Fragment;

import com.huzaifashahbaz.viewpagerapp.R;

public class CounterFragment extends Fragment {
    private TextView tvCount;
    private int count = 0;
    @Nullable
    @Override
    public View onCreateView(@NonNull LayoutInflater inflater, @Nullable ViewGroup container, @Nullable Bundle savedInstanceState) {
        View view = inflater.inflate(R.layout.fragment_counter, container, false);
        tvCount = view.findViewById(R.id.text_view_count);
        Button btnCount = view.findViewById(R.id.button_count);
        Button btnReset = view.findViewById(R.id.button_reset);
        btnCount.setOnClickListener(v -> {
            count++;
            tvCount.setText("Count: " + count);
        });
        btnReset.setOnClickListener(v -> {
            count = 0;
            tvCount.setText("Count: " + count);
        });
        return view;
    }
}