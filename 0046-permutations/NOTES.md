in python code we actually need to append a shallow copy of cur to ans using cur[:] because otherwise a reference is present in the list ans which iis changed when any change is made to cur