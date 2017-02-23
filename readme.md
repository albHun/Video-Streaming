# Hashcode - randomisation implementation

## Naming conventions and data structure

- Output data structure: each out put is a list of lists:
```
    test_caches = [
                    [2],    // server 0 stores video 2
                    [3,1],  // server 1 stored videos 3 and 1
                    [0,1]   //Cache server 2 contains videos 0 and 1.
                ]
```