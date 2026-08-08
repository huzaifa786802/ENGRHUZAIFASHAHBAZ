package TasbeehSQLidatabase;
package TasbeehSQLidatabase;

import android.database.Cursor;
import android.os.Bundle;
import androidx.fragment.app.Fragment;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ListView;
import android.widget.SimpleCursorAdapter;
public class HistoryFragment extends Fragment {
    private DatabaseHelper databaseHelper;
    private ListView listViewHistory;

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState) {
        // Inflate the layout for this fragment
        View view = inflater.inflate(R.layout.fragment_history, container, false);
        listViewHistory = view.findViewById(R.id.list_view_history);
        databaseHelper = new DatabaseHelper(getActivity());
        displayHistory();
        return view;
    }
    private void displayHistory() {
        Cursor cursor = databaseHelper.getAllHistory();
        if (cursor != null) {
            String[] from = new String[]{"count", "timestamp"};
            int[] to = new int[]{android.R.id.text1, android.R.id.text2};

            SimpleCursorAdapter adapter = new SimpleCursorAdapter(getActivity(),
                    android.R.layout.simple_list_item_2, cursor, from, to, 0);

            listViewHistory.setAdapter(adapter);

            // Close the cursor to avoid memory leaks
            cursor.close();
        }
    }
}