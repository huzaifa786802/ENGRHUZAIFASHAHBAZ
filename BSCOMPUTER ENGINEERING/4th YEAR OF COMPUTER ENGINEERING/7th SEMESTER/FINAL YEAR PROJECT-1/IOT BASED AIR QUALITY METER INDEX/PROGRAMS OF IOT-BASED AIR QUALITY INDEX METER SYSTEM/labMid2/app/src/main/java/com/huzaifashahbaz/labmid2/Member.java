package com.huzaifashahbaz.labmid2;

public class Member {
    private String name;
    private String role;
    private String experience;

    public Member(String name, String role, String experience) {
        this.name = name;
        this.role = role;
        this.experience = experience;
    }

    public String getName() { return name; }
    public String getRole() { return role; }
    public String getExperience() { return experience; }
}
