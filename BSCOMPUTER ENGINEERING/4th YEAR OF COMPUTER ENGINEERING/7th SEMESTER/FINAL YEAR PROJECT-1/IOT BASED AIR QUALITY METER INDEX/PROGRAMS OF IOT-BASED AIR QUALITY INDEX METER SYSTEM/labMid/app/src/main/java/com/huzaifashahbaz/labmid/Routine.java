package com.huzaifashahbaz.labmid;

import java.io.Serializable;

public class Routine implements Serializable {
    private String name;
    private String timeEstimate;
    private String type;
    private String urgency;
    private String date;
    private boolean isMorningTask;
    private boolean hasReminder;
    private int rating;

    public Routine(String name, String timeEstimate, String type, String urgency, String date,
                   boolean isMorningTask, boolean hasReminder, int rating) {
        this.name = name;
        this.timeEstimate = timeEstimate;
        this.type = type;
        this.urgency = urgency;
        this.date = date;
        this.isMorningTask = isMorningTask;
        this.hasReminder = hasReminder;
        this.rating = rating;
    }

    public String getName() { return name; }
    public String getTimeEstimate() { return timeEstimate; }
    public String getType() { return type; }
    public String getUrgency() { return urgency; }
    public String getDate() { return date; }
    public boolean isMorningTask() { return isMorningTask; }
    public boolean hasReminder() { return hasReminder; }
    public int getRating() { return rating; }
}
