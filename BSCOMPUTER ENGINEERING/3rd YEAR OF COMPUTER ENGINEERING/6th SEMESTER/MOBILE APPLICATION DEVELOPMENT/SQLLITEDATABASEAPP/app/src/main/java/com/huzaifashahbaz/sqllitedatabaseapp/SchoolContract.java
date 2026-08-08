package com.huzaifashahbaz.sqllitedatabaseapp;
public final class SchoolContract {
    public static class Student {
        public static final String TABLE_NAME = "student";
        public static final String COLUMN_ID = "id";
        public static final String COLUMN_NAME = "name";
        public static final String COLUMN_ADDRESS = "address";
        public static final String CREATE_STUDENT_TABLE =
                "CREATE TABLE " + TABLE_NAME + "(" +
                        COLUMN_ID + " INTEGER PRIMARY KEY, " +
                        COLUMN_NAME + " TEXT, " +
                        COLUMN_ADDRESS + " TEXT) ";
        public static final String DELETE_STUDENT_TABLE =
                "DROP TABLE IF EXISTS " + TABLE_NAME;
        public static final String READ_ALL_TABLE = "SELECT * FROM " +
                TABLE_NAME;
    }
}