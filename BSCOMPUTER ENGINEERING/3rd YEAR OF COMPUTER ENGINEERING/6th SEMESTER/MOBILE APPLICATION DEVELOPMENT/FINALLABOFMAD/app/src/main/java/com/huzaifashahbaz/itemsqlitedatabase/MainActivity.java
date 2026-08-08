package com.huzaifashahbaz.itemsqlitedatabase;//package of itemsqlitedatadbase
import android.os.Bundle;//bundle class
import android.view.View;//view class
import android.widget.ArrayAdapter;//array adapter
import android.widget.Button;//button class
import android.widget.EditText;//edittext class
import android.widget.ListView;//listview class
import androidx.appcompat.app.AppCompatActivity;//AppCompatActivity class
import java.util.ArrayList;//array list class
public class MainActivity extends AppCompatActivity {//main activity function
    private EditText editTextID, editTextItem, editTextQuantity, editTextPrice;//data members of edittext private class
    private Button btnAddToList;//data memebers of button private class
    private ListView listView;//data members of listview private class
    private ArrayList<String> itemList;//data members of item list of array list private class
    private ArrayAdapter<String> adapter;//data members of arrayadapter [rivate class
    @Override
    protected void onCreate(Bundle savedInstanceState) {//on create function
        super.onCreate(savedInstanceState);//saved instance state of bundle
        setContentView(R.layout.activity_main);//main activity java file create
        editTextID = findViewById(R.id.editTextID);//id java file created
        editTextItem = findViewById(R.id.editTextItem);//item java file created
        editTextQuantity = findViewById(R.id.editTextQuantity);//qunatity java file created
        editTextPrice = findViewById(R.id.editTextPrice);//price java file created
        btnAddToList = findViewById(R.id.btnaddtolist);//addtolist java file created
        listView = findViewById(R.id.list_item);//list_item java file created
        itemList = new ArrayList<>();//item list declares the itemList
        adapter = new ArrayAdapter<>(this, android.R.layout.simple_list_item_1, itemList);//simplelistitem java file created,adapter toast message
        listView.setAdapter(adapter);//set adapter of the listview
        btnAddToList.setOnClickListener(new View.OnClickListener() {//btnaddtolist onClick listener function
            @Override
            public void onClick(View v) {//onclick function of btnaddtolist
                addToList();
            }
        });
    }
    public void addToList() {//addtolistfunction
        //now we make sql table of user input interface
        String id = editTextID.getText().toString();//string id declare to database table
        String item = editTextItem.getText().toString();//string item declare to database table
        String quantity = editTextQuantity.getText().toString();//string  quantity declare to database table
        String price = editTextPrice.getText().toString();//string  price declare to database table
        String listItem = "ID: " + id + ", Item: " + item + ", Quantity: " + quantity + ", Price: " + price;//string listitem declare to database table
        itemList.add(listItem);//declare the itemlist sql database table
        adapter.notifyDataSetChanged();//datasetchanged of sql database
        // Clear the input fields after adding the item
        editTextID.setText("");
        editTextItem.setText("");
        editTextQuantity.setText("");
        editTextPrice.setText("");
    }
}