package com.huzaifashahbaz.notepadapp;
import java.io.Serializable;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Locale;
public class Note implements Serializable {
    private String content;
    private String dateTime;
    public Note(String content) {
        this.content = content;
        this.dateTime = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss", Locale.getDefault()).format(new Date());
    }
    public String getContent() {
        return content;
    }
    public String getDateTime() {
        return dateTime;
    }
}