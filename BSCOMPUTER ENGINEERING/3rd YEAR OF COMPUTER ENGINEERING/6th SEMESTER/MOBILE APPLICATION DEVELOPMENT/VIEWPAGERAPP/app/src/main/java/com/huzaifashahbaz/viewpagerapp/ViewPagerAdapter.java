package com.huzaifashahbaz.viewpagerapp;
import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.fragment.app.Fragment;
import androidx.fragment.app.FragmentManager;
import androidx.fragment.app.FragmentPagerAdapter;
public  class ViewPagerAdapter extends FragmentPagerAdapter{
    public ViewPagerAdapter(FragmentManager fm)
    {
        super(fm);
    }
    @NonNull
    @Override
    public Fragment getItem(int position)
    {
        if (position==0)
        {
            return new FragmentA();
        }
        else if(position==1)
        {
            return new FragmentB();
        }
        else
        {
            return null;
        }
    }
    @Override
    public int getCount()
    {
        return 2;
    }
    @Nullable
    @Override
    public CharSequence getPageTitle(int position)
    {
        if(position==0)
        {
            return "FragmnetA";
        }
        else if (position==1)
        {
            return "FragmentB";
        }
        else
        {
            return null;
        }
    }
}