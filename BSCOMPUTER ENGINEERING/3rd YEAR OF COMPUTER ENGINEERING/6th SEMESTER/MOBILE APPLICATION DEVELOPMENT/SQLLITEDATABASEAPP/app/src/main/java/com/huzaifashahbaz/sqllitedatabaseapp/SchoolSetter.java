package com.huzaifashahbaz.sqllitedatabaseapp;

public class SchoolSetter {
    int id;
    String name;
    String address;
    public SchoolSetter(int id,String name,String address)
    {
        this.id=id;
        this.name=name;
        this.address=address;
    }
    public int getId()
    {
        return id;
    }
    public String getName()
    {
        return name;
    }
    public String getAddress()
    {
        return address;
    }
}
