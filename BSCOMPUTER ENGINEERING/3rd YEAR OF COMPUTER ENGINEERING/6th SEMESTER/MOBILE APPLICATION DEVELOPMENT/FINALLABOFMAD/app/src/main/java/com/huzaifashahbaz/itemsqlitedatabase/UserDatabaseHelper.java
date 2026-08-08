package com.huzaifashahbaz.itemsqlitedatabase;//package of itemsqlitedatadbase
import android.content.ContentValues;//context values class
import android.content.Context;//context class
import android.database.Cursor;//cursor class
import android.database.sqlite.SQLiteDatabase;//sqlite database class
import android.database.sqlite.SQLiteOpenHelper;//sqlite openhelper class
public class UserDatabaseHelper extends SQLiteOpenHelper {//userdatabasehelper function
    private static final String DATABASE_NAME = "userDatabase.db";//userdatabase table
    private static final int DATABASE_VERSION = 1;//version table
    private static final String TABLE_USERS = "users";//users table name
    // Columns
    private static final String COLUMN_ID = "id";//column id of sqlite database table
    private static final String COLUMN_ITEM = "item";//column item of sqlite database table
    private static final String COLUMN_QUANTITY = "quantity";//column quantity of sqlite database table
    private static final String COLUMN_PRICE = "price";////column price of sqlite database table
    // Create table SQL query of user database
    private static final String TABLE_CREATE =
            "CREATE TABLE " + TABLE_USERS + " (" +
                    COLUMN_ID + " INTEGER PRIMARY KEY AUTOINCREMENT, " +
                    COLUMN_ITEM + " TEXT, " +
                    COLUMN_QUANTITY + " TEXT, " +
                    COLUMN_PRICE + " TEXT" +
                    ");";
    public UserDatabaseHelper(Context context) {//userdatabase helper function calles
        super(context, DATABASE_NAME, null, DATABASE_VERSION);//super context of userdatabasehelper
    }
    @Override
    public void onCreate(SQLiteDatabase db) {//oncreate function called
        db.execSQL(TABLE_CREATE);
    }
    @Override
    public void onUpgrade(SQLiteDatabase db, int oldVersion, int newVersion) {//onUpgrade function
        db.execSQL("DROP TABLE IF EXISTS " + TABLE_USERS);
        onCreate(db);
    }
    // Insert a new user record of user dtabase table
    public boolean addUser(String item, String quantity, String price) {//boolean adduser function called
        SQLiteDatabase db = this.getWritableDatabase();//writeable database
        ContentValues values = new ContentValues();//new contnet values of user database table
        values.put(COLUMN_ITEM, item);// add values
        values.put(COLUMN_QUANTITY, quantity);//add value
        values.put(COLUMN_PRICE, price);//add values
        long result = db.insert(TABLE_USERS, null, values);
        db.close();
        return result != -1;
    }
    // Retrieve all user records of user database table
    public Cursor getAllUsers() {//getallusers function called
        SQLiteDatabase db = this.getReadableDatabase();
        return db.rawQuery("SELECT * FROM " + TABLE_USERS, null);
    }
    // Update a user record of user database table
    public boolean updateUser(int id, String item, String quantity, String price) {//boolean updateuser function called
        SQLiteDatabase db = this.getWritableDatabase();
        ContentValues values = new ContentValues();
        values.put(COLUMN_ITEM, item);
        values.put(COLUMN_QUANTITY, quantity);
        values.put(COLUMN_PRICE, price);
        int result = db.update(TABLE_USERS, values, COLUMN_ID + " = ?", new String[]{String.valueOf(id)});
        db.close();
        return result > 0;
    }
    // Delete a user record of user datadbase table
    public boolean deleteUser(int id) {//delete user function called
        SQLiteDatabase db = this.getWritableDatabase();//writeableDatabase of SQLiteDatabase
        int result = db.delete(TABLE_USERS, COLUMN_ID + " = ?", new String[]{String.valueOf(id)});
        db.close();
        return result > 0;
    }
    public boolean insertUser(int id) {//insert user database function called
        SQLiteDatabase db = this.getWritableDatabase();//writeableDatabase
        ContentValues values = new ContentValues();//content values
        values.put(COLUMN_ID, id); // Assuming COLUMN_ID is a string constant
        long result = db.insert(TABLE_USERS, null, values);//long reuslt of user database helper
        db.close();
        return result > 0;
    }
}