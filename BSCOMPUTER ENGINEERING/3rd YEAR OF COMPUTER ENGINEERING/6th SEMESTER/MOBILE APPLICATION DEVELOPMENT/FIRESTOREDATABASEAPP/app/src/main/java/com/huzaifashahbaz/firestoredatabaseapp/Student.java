package com.huzaifashahbaz.firestoredatabaseapp;
public class Student {
    private String registrationNumber;
    private String name;
    private String parentPhone;
    private String address;
    public Student() {}
    public Student(String registrationNumber, String name, String parentPhone, String address) {
        this.registrationNumber = registrationNumber;
        this.name = name;
        this.parentPhone = parentPhone;
        this.address = address;
    }
    public String getRegistrationNumber() {
        return registrationNumber;
    }
    public void setRegistrationNumber(String registrationNumber) {
        this.registrationNumber = registrationNumber;
    }
    public String getName() {
        return name;
    }
    public void setName(String name) {
        this.name = name;
    }
    public String getParentPhone() {
        return parentPhone;
    }
    public void setParentPhone(String parentPhone) {
        this.parentPhone = parentPhone;
    }
    public String getAddress() {
        return address;
    }
    public void setAddress(String address) {
        this.address = address;
    }
}