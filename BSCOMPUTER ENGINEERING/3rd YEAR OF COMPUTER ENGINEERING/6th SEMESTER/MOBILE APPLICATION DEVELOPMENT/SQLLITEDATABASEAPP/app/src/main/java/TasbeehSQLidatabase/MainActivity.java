package TasbeehSQLidatabase;
import android.annotation.SuppressLint;
import android.database.Cursor;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;
import android.widget.Toast;
import androidx.appcompat.app.AppCompatActivity;
import androidx.viewpager.widget.ViewPager;
import androidx.fragment.app.Fragment;
import androidx.fragment.app.FragmentManager;
import androidx.fragment.app.FragmentPagerAdapter;

import com.huzaifashahbaz.sqllitedatabaseapp.R;

public class MainActivity extends AppCompatActivity {
    TextView tvCount;
    Button btnCount, btnReset, btnViewHistory;
    int Count = 0;
    DatabaseHelper databaseHelper;
    ViewPager viewPager;
    HistoryPagerAdapter pagerAdapter;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        tvCount=findViewById(R.id.text_view_count);
        btnCount = findViewById(R.id.button_count);
        btnReset = findViewById(R.id.button_reset);
        btnViewHistory = findViewById(R.id.button_view_history);
        viewPager = findViewById(R.id.view_pager);
        databaseHelper = new DatabaseHelper(this);
        pagerAdapter = new HistoryPagerAdapter(getSupportFragmentManager());
        viewPager.setAdapter(pagerAdapter);
        viewPager.setOffscreenPageLimit(1); // Cache one page on each side
    }
    public void onPressResetbtn(View view) {
        Count = 0;
        tvCount.setText("Count: " + Count);
    }
    public void onPressHistorybtn(View view) {
        Toast.makeText(this, "JAZAKALLAH KHAIR", Toast.LENGTH_SHORT).show();
        viewPager.setCurrentItem(0);
    }
    public void onPressCountbtn(View view) {
        Count++;
        tvCount.setText("Count: " + Count);
        databaseHelper.insertCount(Count);
    }
    private class HistoryPagerAdapter extends FragmentPagerAdapter {
        public HistoryPagerAdapter(FragmentManager fm) {
            super(fm);
        }
        @Override
        public Fragment getItem(int position) {
            return new HistoryFragment();
        }
        @Override
        public int getCount() {
            return 1; // Number of tabs/pages
        }
        @Override
        public CharSequence getPageTitle(int position) {
            return "History";
        }
    }
}