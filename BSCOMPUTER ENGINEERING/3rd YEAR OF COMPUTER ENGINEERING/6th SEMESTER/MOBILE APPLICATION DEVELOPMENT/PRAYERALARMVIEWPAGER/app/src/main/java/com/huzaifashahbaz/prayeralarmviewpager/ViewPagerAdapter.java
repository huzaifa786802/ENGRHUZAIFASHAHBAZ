package com.huzaifashahbaz.prayeralarmviewpager;
import androidx.annotation.NonNull;
import androidx.fragment.app.Fragment;
import androidx.fragment.app.FragmentActivity;
import androidx.viewpager2.adapter.FragmentStateAdapter;
public class ViewPagerAdapter extends FragmentStateAdapter {
    private static final int NUM_PAGES = 5;
    public ViewPagerAdapter(@NonNull FragmentActivity fragmentActivity) {
        super(fragmentActivity);
    }
    @NonNull
    @Override
    public Fragment createFragment(int position) {
        // Create a new instance of PrayerFragment with appropriate text for each page
        return PrayerFragment.newInstance("Prayer Time " + (position + 1));
    }
    @Override
    public int getItemCount() {
        // Return the number of pages
        return NUM_PAGES;
    }
}