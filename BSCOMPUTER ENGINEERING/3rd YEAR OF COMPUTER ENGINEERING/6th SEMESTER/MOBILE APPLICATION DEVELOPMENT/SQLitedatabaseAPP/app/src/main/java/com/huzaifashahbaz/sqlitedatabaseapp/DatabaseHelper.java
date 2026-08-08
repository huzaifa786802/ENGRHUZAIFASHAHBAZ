package com.huzaifashahbaz.sqlitedatabaseapp;
import android.content.ContentValues;
import android.content.Context;
import android.database.Cursor;
import android.database.sqlite.SQLiteDatabase;
import android.database.sqlite.SQLiteOpenHelper;
public class DatabaseHelper extends SQLiteOpenHelper {
    private static final String DATABASE_NAME="student.db";
    private static final String TABLE_NAME="student_table";
    private static final String COL_1="REGISTERATION_NUMBER";
    private static final String COL_2="NAME";
    private static final String COL_3="PARENT_PHONE";
    private static final String COL_4="ADDRESS";
    public DatabaseHelper(Context context)
    {
        super(context,DATABASE_NAME,null,1);
    }
    @Override
    public void onCreate(SQLiteDatabase db)
    {
        db.execSQL("CREATE TABLE " + TABLE_NAME + "(REGISTERATION_NUMBER INTEGER PRIMARY KEY,NAME TEXT,PARENT_PHONE TEXT,ADDRESS TEXT)");
    }
    @Override
    public void onUpgrade(SQLiteDatabase db,int oldVersion,int newVersion)
    {
        db.execSQL("DROP TABLE IF EXISTS "+ TABLE_NAME);
        onCreate(db);
    }
    public boolean insertData(String regNumber,String name,String parentPhone,String address)
    {
        SQLiteDatabase db = this.getWritableDatabase();
        ContentValues contentValues = new ContentValues();
        contentValues.put(COL_1, regNumber);
        contentValues.put(COL_2, name);
        contentValues.put(COL_3, parentPhone);
        contentValues.put(COL_4, address);
        long result = db.insert(TABLE_NAME, null, contentValues);
        return result != -1;
    }
    public Cursor searchByNme(String name)
    {
        SQLiteDatabase db=this.getWritableDatabase();
        return db.rawQuery("SELECT * FROM " + TABLE_NAME + " WHERE NAME LIKE ?", new String[]{"%" + name + "%"});
    }
    public Cursor searchByRegNumber(String regNumber)
    {
        SQLiteDatabase db = this.getWritableDatabase();
        return db.rawQuery("SELECT * FROM " + TABLE_NAME + " WHERE REGISTRATION_NUMBER = ?", new String[]{regNumber});
    }
}
