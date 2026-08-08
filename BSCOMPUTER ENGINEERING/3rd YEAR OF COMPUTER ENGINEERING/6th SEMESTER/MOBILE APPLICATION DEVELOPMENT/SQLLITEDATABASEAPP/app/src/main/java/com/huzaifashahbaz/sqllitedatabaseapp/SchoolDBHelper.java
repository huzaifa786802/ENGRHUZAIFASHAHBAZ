package com.huzaifashahbaz.sqllitedatabaseapp;
import android.content.ContentValues;
import android.content.Context;
import android.database.Cursor;
import android.database.sqlite.SQLiteDatabase;
import android.database.sqlite.SQLiteOpenHelper;
import android.widget.Toast;
import androidx.annotation.Nullable;
import java.util.ArrayList;
public class SchoolDBHelper extends SQLiteOpenHelper {
    Context context;
    public static final int DATABASE_VERSION = 1;
    public static final String DATABASE_NAME = "School.db";
    public SchoolDBHelper(@Nullable Context context) {
        super(context, DATABASE_NAME, null, DATABASE_VERSION);
        this.context = context;
    }
    @Override
    public void onCreate(SQLiteDatabase db) {
        db.execSQL(SchoolContract.Student.CREATE_STUDENT_TABLE);
    }
    @Override
    public void onUpgrade(SQLiteDatabase db, int oldVersion, int newVersion) {
        db.execSQL(SchoolContract.Student.DELETE_STUDENT_TABLE);
        onCreate(db);
    }
    public void addEntry(int id, String name, String address){
        SQLiteDatabase db = getWritableDatabase();
        ContentValues values = new ContentValues();
        values.put(SchoolContract.Student.COLUMN_ID, id);
        values.put(SchoolContract.Student.COLUMN_NAME, name);
        values.put(SchoolContract.Student.COLUMN_ADDRESS, address);
        try{
            db. insertOrThrow (SchoolContract.Student.TABLE_NAME, null, values);
        }catch (Exception e){
            Toast.makeText(context, "Error: " + e, Toast.LENGTH_SHORT).show();
        }
        db.close();
    }
    public ArrayList<SchoolSetter> readAll(){
        SQLiteDatabase db = getWritableDatabase();
        Cursor cursor = db.rawQuery(SchoolContract.Student.READ_ALL_TABLE,null);
        ArrayList<SchoolSetter> setters = new ArrayList<SchoolSetter>();
        while (cursor.moveToNext()){
            setters.add(new SchoolSetter(cursor.getInt(0), cursor.getString(1), cursor.getString(2))
            );
        }
        return setters;
    }
}