==========
Linux Disk
==========


LVM -- Logical volume management
================================


.. sidebar:: Terminologies

    Every thing have an UUID
    
    - **PE** -- Physical Extend, smallest element, default size 4MB
    - **PV** -- Physical Volume
    - **VG** -- Volume Group
    - **LV** -- Logic Volume

In computer storage, *logical volume management* or LVM provides a method of *allocating space* on mass-storage devices that is *more flexible* than conventional partitioning schemes. In particular, a volume manager can **concatenate**, **stripe together** or otherwise **combine partitions** (or block devices in general) into larger virtual ones that administrators can re-size or move, *potentially without interrupting system use*. [#]_

.. image:: images/lvm.svg
    :align: center


Management
----------

.. sidebar:: Note

    /dev/vg0/lv0 --> /dev/vg0-lv0

- Create a Logic Volume: ``pvcreate`` --> ``vgcreate`` --> ``lvcreate`` --> ``mkfs.ext3`` --> ``mount``

.. code-block:: bash
    :linenos:

    pvcreate /dev/sda5 dev/sda6
    vgcreate vg0 /dev/sda5 /dev/sda6
    lvcreate -L 800M -n lv0 vg0
    mkfs.ext3 /dev/vg0/lv0 
    mount /dev/vg0/lv0 /mnt``

- Delete a Logic Volume: ``lvremove`` --> ``vgremove`` --> ``pvremove``

.. code-block:: bash
    :linenos:

    lvremove lv0
    vgremove vg0
    pvremove /dev/sda5 dev/sda6

- Expand Logic Volume: ``lvextend`` --> ``resize2fs``

.. code-block:: bash
    :linenos:

    lvextend -L +400M /dev/vg0/lv0 
    resize2fs /mnt

- Reduce Logic Volume: ``umount`` --> ``e2fsck`` --> ``resize2fs`` --> ``lvreduce``

.. code-block:: bash
    :linenos:

    umount /mnt
    e2fsck -f /dev/vg0/lv0
    resize2fs /dev/vg0/lv0 180M   #file system resize to a smaller size
    lvreduce -L 1000M /dev/vg0/lv0   #reduce to 1000M

- Add PV: ``vgextend``

.. code-block:: bash
    :linenos:

    pvcreate /dev/sda8
    vgextend vg0 /dev/sda8


- Remove PV: ``pvmove``

.. code-block:: bash
    :linenos:

    pvmove /dev/sda6   #move PE to out of sda6(PV)
    vgreduce vg0 /dev/sda6   #reduce one or more unused PV
    pvremove /dev/sda6

- Currently we are using **lvm2**
    - check lvm version: ``vgscan``
    - convert lvm1 VG to lvm2 VG: ``vgconvert -M2 vg0``

Check lvm infos
---------------

.. code-block:: bash
    :linenos:
    :emphasize-lines: 1,6,11,15,38,81
 
    $ pvs
    PV         VG                        Fmt  Attr PSize  PFree 
    /dev/loop1 stack-volumes-default     lvm2 a--  10.01g 10.01g
    /dev/loop2 stack-volumes-lvmdriver-1 lvm2 a--  10.01g  8.00m

    $ vgs
    VG                        #PV #LV #SN Attr   VSize  VFree 
    stack-volumes-default       1   0   0 wz--n- 10.01g 10.01g
    stack-volumes-lvmdriver-1   1   1   0 wz--n- 10.01g  8.00m

    $ lvs
    LV                                          VG                        Attr       LSize  Pool Origin Data%  Meta%  Move Log Cpy%Sync Convert
    volume-c86ee1fc-0881-4b85-aa8a-432f8ad1c9cb stack-volumes-lvmdriver-1 -wi-ao---- 10.00g                                                 

    $ pvdisplay
    --- Physical volume ---
    PV Name               /dev/loop1
    VG Name               stack-volumes-default
    PV Size               10.01 GiB / not usable 2.00 MiB
    Allocatable           yes 
    PE Size               4.00 MiB
    Total PE              2562
    Free PE               2562
    Allocated PE          0
    PV UUID               dohGEH-212L-10Nb-wiWQ-mjZ4-ApKS-AchT26
    
    --- Physical volume ---
    PV Name               /dev/loop2
    VG Name               stack-volumes-lvmdriver-1
    PV Size               10.01 GiB / not usable 2.00 MiB
    Allocatable           yes 
    PE Size               4.00 MiB
    Total PE              2562
    Free PE               2
    Allocated PE          2560
    PV UUID               UdQnN2-ddmJ-w3az-Gzp3-b7pf-tIFS-IB8Pho
     
    $ vgdisplay
    --- Volume group ---
    VG Name               stack-volumes-default
    System ID             
    Format                lvm2
    Metadata Areas        1
    Metadata Sequence No  1
    VG Access             read/write
    VG Status             resizable
    MAX LV                0
    Cur LV                0
    Open LV               0
    Max PV                0
    Cur PV                1
    Act PV                1
    VG Size               10.01 GiB
    PE Size               4.00 MiB
    Total PE              2562
    Alloc PE / Size       0 / 0   
    Free  PE / Size       2562 / 10.01 GiB
    VG UUID               VWeopN-dnmk-W6Gg-byZE-JwRw-hndS-9xa5LU
     
    --- Volume group ---
    VG Name               stack-volumes-lvmdriver-1
    System ID             
    Format                lvm2
    Metadata Areas        1
    Metadata Sequence No  2
    VG Access             read/write
    VG Status             resizable
    MAX LV                0
    Cur LV                1
    Open LV               1
    Max PV                0
    Cur PV                1
    Act PV                1
    VG Size               10.01 GiB
    PE Size               4.00 MiB
    Total PE              2562
    Alloc PE / Size       2560 / 10.00 GiB
    Free  PE / Size       2 / 8.00 MiB
    VG UUID               5TTHgC-LXzV-7i9u-YXnG-KQTY-HXmD-SFocsq

    $ lvdisplay    
    --- Logical volume ---
    LV Path                /dev/stack-volumes-lvmdriver-1/volume-c86ee1fc-0881-4b85-aa8a-432f8ad1c9cb
    LV Name                volume-c86ee1fc-0881-4b85-aa8a-432f8ad1c9cb
    VG Name                stack-volumes-lvmdriver-1
    LV UUID                KSvISz-D19i-13Ra-ZCVj-tkSa-dco6-uX7PJ2
    LV Write Access        read/write
    LV Creation host, time r16s12, 2015-05-28 16:35:27 +0800
    LV Status              available
    # open                 1
    LV Size                10.00 GiB
    Current LE             2560
    Segments               1
    Allocation             inherit
    Read ahead sectors     auto
    - currently set to     256
    Block device           253:0
     



RAID
====


Disk Performance
================


dd -- convert and copy a file
-----------------------------

The dd utility copies the standard input to the standard output.  Input data is read and written in 512-byte blocks.  If input reads are short, input from multiple reads are aggregated to form the output block.  When finished, dd displays the number of complete and partial input and output blocks and truncated input records to the standard error output.


======== ==========================================
Option   description
======== ==========================================
bs=BYTES read and write up to BYTES bytes at a time
count=N  copy only N input blocks
======== ==========================================

::

    dd if=/dev/zero of=testfile bs=1M count=512 conv=fdatasync


.. [#] http://en.wikipedia.org/wiki/Logical_volume_management
