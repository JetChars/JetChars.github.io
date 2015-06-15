==========
Linux Disk
==========



.. sidebar:: e2fsprogs
  
    e2fs programs, toolkits for maintaining ext2/3/4 filesystem
        
    - **mke2fs** - create filesystem
   
    - **mkfs.ext{2,3,4}** -- quickly make a filesystem
    
    - **dumpe2fs** -- check filesystem info
    
    - **e2label** -- tag a device, for partition management ``e2lable /dev/sdb1 wenj``
    
    - **e2fsck** -- check filesystem's integrity
    
    - **resize2fs** -- autoresize filesystem size
    
    - **tune2fs** -- change filesystem related parameters
    
    - **debugfs** -- debug a filesystem, can check or change it's status


Filesystem
==========

Kernnel -- VFS
--------------

Short for **Virtual File System**, or **Virtual Filesystem Switch**, maintain tree shaped linux filesystem

- It's a glue level between storage media and filesystem, let system calls like ``open()`` ``read()`` ``write()`` don't need to know to realize it in lower level
- Sometimes short for **Stackable Filesystem** , because it can combine different filesystem seamlessly
- Use command like ``mount`` to manage filesystem


Driver
------

::

    ls /lib/modules/3.10.0-123.el7.x86_64/kernel/fs/
    binfmt_misc.ko  dlm      fuse   mbcache.ko  pstore
    btrfs           exofs    gfs2   nfs         squashfs
    cachefiles      ext4     isofs  nfs_common  udf
    cifs            fat      jbd2   nfsd        xfs
    cramfs          fscache  lockd  nls


============== =======================
type           items
============== =======================
local          ext2/3/4
network        sambafs/cifs/nfs/sshfs/gmailfs
cluster        gfs gfs2 ocfs
distributed    HDFS mfs
============== =======================


mke2fs  
^^^^^^

============= ============================ ========================
option        description                  examples
============= ============================ ========================
-t            specify filesys type         mke2fs -t ext4 /dev/sda3
-b blocksize  specify block size
-c            check when creating filesys
-L label      specify volume label
-j            create journal system        ext2 doesn't contain jornal ext3/4 built-in journal sys
============= ============================ ========================
 



Devices
-------
  
Storage Cards
^^^^^^^^^^^^^

``RAID/HBA``  

Serial Devices
^^^^^^^^^^^^^^

``SATA`` ``SCSI`` ``SAS`` ``USB`` name as ``sd[a-z]``

Network Storage
^^^^^^^^^^^^^^^

``SAN(Storage Area Network)`` 


Mount
=====

.. sidebar:: Note

    **mount.ntfs**

    ubuntu's built-in NTFS driver, rhel/centos/fedora user need download ``fuse-ntfs``::

        mount.ntfs /dev/sdd /mnt

    **fuser**

    compared w/ lsof, fuser can check which process use folder or file exactly

    - ``-v`` show more details
    - ``-u`` display user IDs
    - ``-l`` show support signal list
    - ``-k -SIGNAL`` send signal to all processes use this file

    ===== =========
    flag  meaning
    ===== =========
    c     as current folder
    e     as executable object
    r     as root
    s     as shared lib
    ===== =========


Mount a device
--------------

::

    mount [-t fstype] [-o mount_opt] device mountpoint


| **Mount Options** -- seperate by comma
|

======= ======================
option  description
======= ======================
ro      readonly
rw      read and write
remount mount -o remount,ro /dev/sdb1 /mnt/
sync    no use memcache
async   default option, use memcache
atime   default option, record access time
noatime not record access time
acl     enable acl, must enabled if use acl
loop    mount iso file
======= ======================



.. cede-block:: bash

    mount  # show mount info
    mkdir /mnt; mke2fs /dev/sda1  # create mountpoint & format filesystem before mount
    mount /dev/sda1 /mnt  # mount sda1 to /mnt


Unmount a device
----------------

::

    $ umount testlvm/ -f
    umount: /root/testlvm: target is busy.
            (In some cases useful info about processes that use
             the device is found by lsof(8) or fuser(1))

    $ fuser -m testlvm/
    /root/testlvm:       24572c

    $ ps aux | grep 24572
    root      24572  0.0  0.0 117056  3924 pts/0    S+   May28   0:01 -bash
    root     210760  0.0  0.0 112644   960 pts/41   S+   09:44   0:00 grep --color=auto 24572c

    $ kill -9 24572
    umount testlvm/    # umount object can be device or mount point


Auto Mount
----------

- configure file ``/etc/fstab`` file system table::

    mount -a  # take effect fstab




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

    - current version is **lvm2**
    - check lvm version: ``vgscan``
    - convert LVMv1 to LVMv2: ``vgconvert -M2 vg0``
    - rename VG vg0 to vg1: ``vgrename vg0 vg1``


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

    # lvextend -L 1000M /dev/vg0/lv0    # extend to 1G
    lvextend -L +400M /dev/vg0/lv0     # extend 400M
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

    # pvmove /dev/sda6:1-20 /dev/sda7   # will on move pe block 1-20 to sda7
    pvmove /dev/sda6   #move PE to out of sda6(PV)
    vgreduce vg0 /dev/sda6   #reduce one or more unused PV
    pvremove /dev/sda6

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
 
Issues
------

1. remove vg after pv been removed

::

    $sudo vgremove r16s03-default
    Incorrect metadata area header checksum on /dev/loop1 at offset 4096
    vg_remove_mdas r16s03-default failed
    
    $ sudo vgremove r16s03-default --force
    /dev/loop1: lseek 4096 failed: Invalid argument
    vg_remove_mdas r16s03-default failed

| **Solution :**
|

::

    sudo pvremove /dev/loop1 -ff

2. lvremove: Logical volume in use

.. code-block:: bash

    $ sudo lvremove /dev/r16s11-lvmdriver-1/volume-daffbf30-30b9-4da3-9d34-de1c658ee38c
    Logical volume r16s11-lvmdriver-1/volume-daffbf30-30b9-4da3-9d34-de1c658ee38c in use.
    $ sudo fuser /dev/r16s11-lvmdriver-1/volume-daffbf30-30b9-4da3-9d34-de1c658ee38c
    /dev/dm-0:           159892
    $ sudo kill -9 159892
    $ sudo umount /dev/r16s11-lvmdriver-1/volume-daffbf30-30b9-4da3-9d34-de1c658ee38c


Loop Device
===========

In Unix-like operating systems, a loop device, vnd (vnode disk), or lofi (loop file interface) is a pseudo-device that makes a file accessible as a block device. [#]_

.. sidebar:: truncate

    shrink or extend the size of a file to the specified size, can be used to create a loop file
    ``truncate -s size file`` ``sudo losetup -f --show /dev/lo0 file``

- Get info::

    losetup loopdev   # show specified loopdev
    losetup -l [-a]   # show loopdev list
    losetup -j file [-o offset]
    losetup -f   # Print first unused loop device

- Delete loop: ``losetup -d loopdev...``

- Delete all used loop devices: ``losetup -D``

- Setup loop device: ``losetup [-o offset] [--sizelimit size] [-p pfd] [-rP] {-f[--show]|loopdev} file``
    - ``-show`` will print device name

- Resize loop device: ``losetup -c loopdev``

RAID
====

raid10
------

.. image:: images/raid10.jpg
    :align: right

Also called raid1+0, build raid1 first then use two raid 1 to build a raid0. different from raid 01.


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
.. [#] http://en.wikipedia.org/wiki/Loop_device
