# Copyright 2023 Elijah Gordon (SLcK) <braindisassemblue@gmail.com>

# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

from stat import *
from os import stat, chmod, getcwd, getlogin, name
from sys import argv
from pwd import getpwuid
from time import ctime
from getopt import getopt, GetoptError


def version():
    
    print("+-----------------------------------------------------------------------------------+")
    print("|  pstatx version 1.0.0, Copyright (C) 2023 Elijah Gordon (SLcK)                    |")
    print("|  pstatx comes with ABSOLUTELY NO WARRANTY; for details                            |")
    print("|  type show w. This is free software, and you are welcome                          |")
    print("|  to redistribute it under certain conditions; type show c                         |")
    print("|  for details.                                                                     |")
    print("+-----------------------------------------------------------------------------------+")


def usage():

    print("Usage: {0} --filename <options>".format(argv[0]))

    print("\nOptions:")
    print("  -h: --help                           Print usage and exit")
    print("  -V: --version                        Print version information and exit")
    print("  -F: --filename                       Filename")
    print("  -D: --is-directory                   Return non-zero if the mode is from a directory")
    print("  -S: --is-special-char                Return non-zero if the mode is from a character special device file")
    print("  -B: --is-block                       Return non-zero if the mode is from a block special device file")
    print("  -R: --is-regular                     Return non-zero if the mode is from a regular file")
    print("  -N: --is-fifo                        Return non-zero if the mode is from a FIFO (named pipe)")
    print("  -L: --is-link                        Return non-zero if the mode is from a symbolic link")
    print("  -M: --is-sock                        Return non-zero if the mode is from a socket")
    print("  -d: --is-door                        Return non-zero if the mode is from a door")
    print("  -P: --is-port                        Return non-zero if the mode is from an event port")
    print("  -W: --is-whiteout                    Return non-zero if the mode is from a whiteout")
    print("  -O: --is-mode                        Return the portion of the file’s mode that can be set by os.chmod()")
    print("  -T: --file-type                      Return the portion of the file’s mode that describes the file type (used by the S_IS*() functions above)")
    print("  -f: --file-mode                      Convert a file’s mode to a string of the form ‘-rwxrwxrwx’")
    print("  -p  --protection-bits                Protection bits")
    print("  -I: --inode-number                   Inode number")
    print("  -i: --device                         Device")
    print("  -H: --hard-links-number              Number of hard links")
    print("  -Z: --byte-size                      Size of file, in bytes")
    print("  -U: --user-id                        Numerical user ID")
    print("  -G: --group-id                       Numerical group ID")
    print("  -A: --recent-access                  Time of most recent access")
    print("  -r: --recent-modification            Time of most recent content modification")
    print("  -C: --metadata-change                Platform dependent; time of most recent metadata change on Unix")
    print("  -a: --atime-ns                       Time of most recent access expressed in nanoseconds as an integer")
    print("  -m: --mtime-ns                       Time of most recent content modification expressed in nanoseconds as an integer")
    print("  -c: --ctime-ns                       Time of most recent metadata change expressed in nanosecond as an integer")
    print("  -n: --allocated-blocks               Number of 512-byte blocks allocated for file")
    print("  -E: --filesystem-blocksize           Filesystem blocksize for efficient file system I/O")
    print("  -t: --type-of-device                 Type of device if an inode device")
    print("  -l: --login-name                     Login name")
    print("  -o: --optional-encrypted-password    Optional encrypted password")
    print("  -u: --name-field                     User name or comment field")
    print("  -g: --home-directory                 User home directory")
    print("  -e: --user-command-interpreter       User command interpreter")
    print("  -s: --if-sock                        Tests if a path is a socket")
    print("  -X: --if-link                        Tests if a path is a Symbolic link")
    print("  -w: --if-regular                     Tests if a path is a regular file")
    print("  -b: --if-block                       Block device")
    print("  --if-directory                       Tests if a path is a directory")
    print("  --if-special-char                    Tests if a path is a character device")
    print("  --if-fifo                            Tests if a path is a FIFO or named pipe")
    print("  --is-uid                             Set UID bit")
    print("  --is-gid                             Set-group-ID bit")
    print("  --sticky-bit                         Sticky bit")
    print("  --mask-owner-perm                    Mask for file owner permissions")
    print("  --owner-read                         Owner has read permission")
    print("  --owner-write                        Owner has write permission")
    print("  --owner-execute                      Owner has execute permission")
    print("  --owner-full                         Owner has read, write and execute permission")
    print("  --mask-group-perm                    Mask for group permissions")
    print("  --group-read                         Group has read permission")
    print("  --group-write                        Group has write permission")
    print("  --group-execute                      Group has execute permission")
    print("  --group-full                         Group has read, write and execute permission")
    print("  --mask-others-perm                   Mask for permissions for others (not in group)")
    print("  --others-read                        Others have read permission")
    print("  --others-write                       Others have write permission")
    print("  --others-execute                     Others have execute permission")
    print("  --others-full                        Others have read, write and execute permission")
    print("  --system-lock                        System V file locking enforcement")
    print("  --owner-v7-read                      Unix V7 synonym for S_IRUSR")
    print("  --owner-v7-write                     Unix V7 synonym for S_IWUSR")
    print("  --owner-v7-execute                   Unix V7 synonym for S_IXUSR")
    print("  --owner-v7-full                      Unix V7 synonym, Owner has read, write and execute permission")
    print("  --operating-system                   Name of the operating system")
    print("  --cwd                                Current working directory")
    print("  --get-login                          Name of the user logged in")


def pstatx():

    try:
        if filename:
            print("-- Filename: ( {0} )".format(filename))
        if is_directory:
            print("-- Directory: ( {0} )".format(S_ISDIR(stat(filename).st_mode)))
        if is_special_char:
            print("-- Character special device file: ( {0} )".format(S_ISCHR(stat(filename).st_mode)))
        if is_block:
            print("-- Path is a block special device file: ( {0} )".format(S_ISBLK(stat(filename).st_mode)))
        if is_regular:
            print("-- File: ( {0} )".format(S_ISREG(stat(filename).st_mode)))
        if is_fifo:
            print("-- FIFO or named pipe: ( {0} )".format(S_ISFIFO(stat(filename).st_mode)))
        if is_link:
            print("-- Symbolic link: ( {0} )".format(S_ISLNK(stat(filename).st_mode)))
        if is_sock:
            print("-- Path is a socket: ( {0} )".format(S_ISSOCK(stat(filename).st_mode)))
        if is_door:
            print("-- Door: ( {0} )".format(S_ISDOOR(stat(filename).st_mode)))
        if is_port:
            print("-- Event port: ( {0} )".format(S_ISPORT(stat(filename).st_mode)))
        if is_whiteout:
            print("-- Whiteout: ( {0} )".format(S_ISWHT(stat(filename).st_mode)))
        if is_mode:
            print("-- File permission bits: ( {0} )".format(oct(S_IMODE(stat(filename).st_mode))))
        if file_type:
            print("-- Bit mask for file type: ( {0} )".format(oct(S_IFMT(stat(filename).st_mode))))
        if file_mode:
            print("-- Mode: ( {0} )".format(filemode(stat(filename).st_mode)))
        if protection_bits:
            print("-- Protection bits: ( {0} )".format(stat(filename).st_mode))
        if inode_number:
            print("-- Inode number: ( {0} )".format(stat(filename).st_ino))
        if device:
            print("-- Device: ( {0} )".format(stat(filename).st_dev))
        if hard_links:
            print("-- Number of hard links: ( {0} )".format(stat(filename).st_nlink))
        if user_id:
            print("-- Numerical user ID: ( {0} )".format(getpwuid(stat(filename).st_uid).pw_gid))
        if group_id:
            print("-- Numerical group ID: ( {0} )".format(getpwuid(stat(filename).st_uid).pw_uid))
        if byte_size:
            print("-- Size of file, in bytes: ( {0} )".format(stat(filename).st_size))
        if recent_access:
            print("-- Time of most recent access: ( {0} )".format(ctime(stat(filename).st_atime)))
        if recent_modification:
            print("-- Time of most recent content modification: ( {0} )".format(ctime(stat(filename).st_mtime)))
        if metadata_change:
            print("-- Platform dependent; time of most recent metadata change on Unix: ( {0} )".format(ctime(stat(filename).st_ctime)))
        if atime_ns:
            print("-- Most recent access in nanoseconds: ( {0} )".format(stat(filename).st_atime_ns))
        if mtime_ns:
            print("-- Most recent content modification in nanoseconds: ( {0} )".format(stat(filename).st_mtime_ns))
        if ctime_ns:
            print("-- Most recent metadata change in nanoseconds: ( {0} )".format(stat(filename).st_ctime_ns))
        if allocated_blocks:
            print("-- Number of 512-byte blocks allocated for file: ( {0} )".format(stat(filename).st_blocks))
        if filesystem_blocksize:
            print("-- Filesystem blocksize for efficient file system I/O: ( {0} )".format(stat(filename).st_blksize))
        if type_of_device:
            print("-- Type of device if an inode device: ( {0} )".format(stat(filename).st_rdev))
        if login_name:
            print("-- Login name: ( {0} )".format(getpwuid(stat(filename).st_uid).pw_name))
        if optional_encrypted_password:
            print("-- Optional encrypted password: ( {0} )".format(getpwuid(stat(filename).st_uid).pw_passwd))
        if name_field:
            print("-- User name or comment field: ( {0} )".format(getpwuid(stat(filename).st_uid).pw_gecos))
        if home_directory:
            print("-- User home directory: ( {0} )".format(getpwuid(stat(filename).st_uid).pw_dir))
        if user_command_interpreter:
            print("-- User command interpreter: ( {0} )".format(getpwuid(stat(filename).st_uid).pw_shell))
        if if_sock:
            print("-- Socket: ( {0} )".format(stat(filename).st_mode & S_IFSOCK == S_IFSOCK))
        if if_link:
            print("-- Symbolic lynk: ( {0} )".format(stat(filename).st_mode & S_IFLNK == S_IFLNK))
        if if_regular:
            print("-- Regular file: ( {0} )".format(stat(filename).st_mode & S_IFREG == S_IFREG))
        if if_block:
            print("-- Block device: ( {0} )".format(stat(filename).st_mode & S_IFBLK == S_IFBLK))
        if if_directory:
            print("-- Directory: ( {0} )".format(stat(filename).st_mode & S_IFDIR == S_IFDIR))
        if if_special_char:
            print("-- Character device: ( {0} )".format(stat(filename).st_mode & S_IFCHR == S_IFCHR))
        if if_fifo:
            print("-- Fifo or named pipe: ( {0} )".format(stat(filename).st_mode & S_IFIFO == S_IFIFO))
        if is_uid:
            chmod(filename, S_ISUID)
            print("-- Setting the UID bit on a file")
        if is_gid:
            chmod(filename, S_ISGID)
            print("-- Setting the GID bit on a file")
        if sticky_bit:
            chmod(filename, S_ISVTX)
            print("-- The file can be renamed or deleted only by the owner of the file")
        if mask_owner_perm:
            chmod(filename, S_IRWXU)
            print("-- Mask for file owner permissions")
        if owner_read:
            chmod(filename, S_IRUSR)
            print("-- Owner has read permission")
        if owner_write:
            chmod(filename, S_IWUSR)
            print("-- Owner has write permission")
        if owner_execute:
            chmod(filename, S_IXUSR)
            print("-- Owner has execute permission")
        if owner_full:
            chmod(filename, S_IRUSR | S_IWUSR | S_IXUSR)
            print("-- Owner has read, write and execute permissions")
        if mask_group_perm:
            chmod(filename, S_IRWXG)
            print("-- Mask for group permissions")
        if group_read:
            chmod(filename, S_IRGRP)
            print("-- Group has read permission")
        if group_write:
            chmod(filename, S_IWGRP)
            print("-- Group has write permission")
        if group_execute:
            chmod(filename, S_IXGRP)
            print("-- Group has execute permission")
        if group_full:
            chmod(filename, S_IRGRP | S_IWGRP | S_IXGRP)
            print("-- Group has read, write and execute permissions")
        if mask_others_perm:
            chmod(filename, S_IRWXO)
            print("-- Mask for permissions for others (not in group)")
        if others_read:
            chmod(filename, S_IROTH)
            print("-- Others have read permission")
        if others_write:
            chmod(filename, S_IWOTH)
            print("-- Others have write permission")
        if others_execute:
            chmod(filename, S_IXOTH)
            print("-- Others have execute permission")
        if others_full:
            chmod(filename, S_IROTH | S_IWOTH | S_IXOTH)
            print("-- Others have read, write and execute permissions")
        if system_lock:
            chmod(filename, S_ENFMT)
            print("-- System V file locked")
        if owner_v7_read:
            chmod(filename, S_IREAD)
            print("-- Owner has read permission (Unix V7)")
        if owner_v7_write:
            chmod(filename, S_IWRITE)
            print("-- Owner has write permission (Unix V7)")
        if owner_v7_execute:
            chmod(filename, S_IEXEC)
            print("-- Owner has execute permission (Unix V7)")
        if owner_v7_full:
            chmod(filename, S_IREAD | S_IWRITE | S_IEXEC)
            print("-- Owner has read, write and execute permissions (Unix V7)")
        if operating_system:
            print("-- Name of OS: ( {0} )".format(name))
        if get_login:
            print("-- Name of the logged in user: ( {0} )".format(getlogin()))
        if cwd:
            print("-- Current working directory: ( {0} )".format(getcwd()))

    except (OSError):
        print("-- {0}: No such file or directory".format(filename))


def main():

    global filename
    filename_flag = False
    filename = ""

    global is_directory
    is_directory = ""

    global is_special_char
    is_special_char = ""

    global is_block
    is_block = ""

    global is_regular
    is_regular = ""

    global is_fifo
    is_fifo = ""

    global is_link
    is_link = ""

    global is_sock
    is_sock = ""

    global is_door
    is_door = ""

    global is_port
    is_port = ""

    global is_whiteout
    is_whiteout = ""

    global is_mode
    is_mode = ""

    global file_type
    file_type = ""

    global file_mode
    file_mode = ""

    global protection_bits
    protection_bits = ""

    global inode_number
    inode_number = ""

    global device
    device = ""

    global hard_links
    hard_links = ""

    global user_id
    user_id = ""

    global group_id
    group_id = ""

    global byte_size
    byte_size = ""

    global recent_access
    recent_access = ""

    global recent_modification
    recent_modification = ""

    global metadata_change
    metadata_change = ""

    global atime_ns
    atime_ns = ""

    global mtime_ns
    mtime_ns = ""

    global ctime_ns
    ctime_ns = ""

    global allocated_blocks
    allocated_blocks = ""

    global filesystem_blocksize
    filesystem_blocksize = ""

    global type_of_device
    type_of_device = ""

    global login_name
    login_name = ""

    global optional_encrypted_password
    optional_encrypted_password = ""

    global name_field
    name_field = ""

    global home_directory
    home_directory = ""

    global user_command_interpreter
    user_command_interpreter = ""

    global if_sock
    if_sock = ""

    global if_link
    if_link = ""

    global if_regular
    if_regular = ""

    global if_block
    if_block = ""

    global if_directory
    if_directory = ""

    global if_special_char
    if_special_char = ""

    global if_fifo
    if_fifo = ""

    global is_uid
    is_uid = ""

    global is_gid
    is_gid = ""

    global sticky_bit
    sticky_bit = ""

    global mask_owner_perm
    mask_owner_perm = ""

    global owner_read
    owner_read = ""

    global owner_write
    owner_write = ""

    global owner_execute
    owner_execute = ""

    global owner_full
    owner_full = ""

    global mask_group_perm
    mask_group_perm = ""

    global group_read
    group_read = ""

    global group_write
    group_write = ""

    global group_execute
    group_execute = ""

    global group_full
    group_full = ""

    global mask_others_perm
    mask_others_perm = ""

    global others_read
    others_read = ""

    global others_write
    others_write = ""

    global others_execute
    others_execute = ""

    global others_full
    others_full = ""

    global system_lock
    system_lock = ""

    global owner_v7_read
    owner_v7_read = ""

    global owner_v7_write
    owner_v7_write = ""

    global owner_v7_execute
    owner_v7_execute = ""

    global owner_v7_full
    owner_v7_full = ""

    global operating_system
    operating_system = ""

    global cwd
    cwd = ""

    global get_login
    get_login = ""

    try:
        opts, args = getopt(argv[1:], "hVF:DSBRNLMdPWOTfpIiHZUGArCamcnEtlougesXwb", ["help", "version", "filename=", "is-directory", "is-special-char", "is-block", "is-regular", "is-fifo", "is-link", "is-sock", "is-door", "is-port", "is-whiteout", "is-mode", "file-type", "file-mode", "protection-bits", "inode-number", "device", "hard-links-number", "user-id", "group-id", "byte-size", "recent-access", "recent-modification", "metadata-change", "atime-ns", "mtime-ns", "ctime-ns", "allocated-blocks", "filesystem-blocksize", "type-of-device", "login-name", "optional-encrypted-password",
                            "name-field", "home-directory", "user-command-interpreter", "if-sock", "if-link", "if-regular", "if-block", "if-directory", "if-special-char", "if-fifo", "is-uid", "is-gid", "sticky-bit", "mask-owner-perm", "owner-read", "owner-write", "owner-execute", "owner-full", "mask-group-perm", "group-read", "group-write", "group-execute", "group-full", "mask-others-perm", "others-read", "others-write", "others-execute", "others-full", "system-lock", "owner-v7-read", "owner-v7-write", "owner-v7-execute", "owner-v7-full", "operating-system", "cwd", "get-login"])

    except GetoptError:
        usage()

    else:
        try:
            for opt, arg in opts:
                if opt in ("-h", "--help"): usage(); exit(1)
                if opt in ("-V", "--version"): version(); exit(1)

                if opt in ("-F", "--filename"): filename = arg; filename_flag = True
                if opt in ("-D", "--is-directory"): is_directory = True
                if opt in ("-S", "--is-special-char"): is_special_char = True
                if opt in ("-B", "--is-block"): is_block = True
                if opt in ("-R", "--is-regular"): is_regular = True
                if opt in ("-N", "--is-fifo"): is_fifo = True
                if opt in ("-L", "--is-link"): is_link = True
                if opt in ("-M", "--is-sock"): is_sock = True
                if opt in ("-d", "--is-door"): is_door = True
                if opt in ("-P", "--is-port"): is_port = True
                if opt in ("-W", "--is-whiteout"): is_whiteout = True
                if opt in ("-O", "--is-mode"): is_mode = True
                if opt in ("-T", "--file-type"): file_type = True
                if opt in ("-f", "--file-mode"): file_mode = True
                if opt in ("-p", "--protection-bits"): protection_bits = True
                if opt in ("-I", "--inode-number"): inode_number = True
                if opt in ("-i", "--device"): device = True
                if opt in ("-H", "--hard-links-number"): hard_links = True
                if opt in ("-Z", "--byte-size"): byte_size = True
                if opt in ("-U", "--user-id"): user_id = True
                if opt in ("-G", "--group-id"): group_id = True
                if opt in ("-A", "--recent-access"): recent_access = True
                if opt in ("-r", "--recent-modification"): recent_modification = True
                if opt in ("-C", "--metadata-change"): metadata_change = True
                if opt in ("-a", "--atime-ns"): atime_ns = True
                if opt in ("-m", "--mtime-ns"): mtime_ns = True
                if opt in ("-c", "--ctime-ns"): ctime_ns = True
                if opt in ("-n", "--allocated-blocks"): allocated_blocks = True
                if opt in ("-E", "--filesystem-blocksize"): filesystem_blocksize = True
                if opt in ("-t", "--type-of-device"): type_of_device = True
                if opt in ("-l", "--login-name"): login_name = True
                if opt in ("-o", "--optional-encrypted-password"): optional_encrypted_password = True
                if opt in ("-u", "--name-field"): name_field = True
                if opt in ("-g", "--home-directory"): home_directory = True
                if opt in ("-e", "--user-command-interpreter"): user_command_interpreter = True
                if opt in ("-s", "--if-sock"): if_sock = True
                if opt in ("-X", "--if-link"): if_link = True
                if opt in ("-w", "--if-regular"): if_regular = True
                if opt in ("-b", "--if-block"): if_block = True
                if opt in ("", "--if-directory"): if_directory = True
                if opt in ("", "--if-special-char"): if_special_char = True
                if opt in ("", "--if-fifo"): if_fifo = True
                if opt in ("", "--is-uid"): is_uid = True
                if opt in ("", "--is-gid"): is_gid = True
                if opt in ("", "--sticky-bit"): sticky_bit = True
                if opt in ("", "--mask-owner-perm"): mask_owner_perm = True
                if opt in ("", "--owner-read"): owner_read = True
                if opt in ("", "--owner-write"): owner_write = True
                if opt in ("", "--owner-execute"): owner_execute = True
                if opt in ("", "--owner-full"): owner_full = True
                if opt in ("", "--mask-group-perm"): mask_group_perm = True
                if opt in ("", "--group-read"): group_read = True
                if opt in ("", "--group-write"): group_write = True
                if opt in ("", "--group-execute"): group_execute = True
                if opt in ("", "--group-full"): group_full = True
                if opt in ("", "--mask-others-perm"): mask_others_perm = True
                if opt in ("", "--others-read"): others_read = True
                if opt in ("", "--others-write"): others_write = True
                if opt in ("", "--others-execute"): others_execute = True
                if opt in ("", "--others-full"): others_full = True
                if opt in ("", "--system-lock"): system_lock = True
                if opt in ("", "--owner-v7-read"): owner_v7_read = True
                if opt in ("", "--owner-v7-write"): owner_v7_write = True
                if opt in ("", "--owner-v7-execute"): owner_v7_execute = True
                if opt in ("", "--owner-v7-full"): owner_v7_full = True
                if opt in ("", "--operating-system"): operating_system = True
                if opt in ("", "--cwd"): cwd = True
                if opt in ("", "--get-login"): get_login = True

            if filename: pstatx()

            elif is_directory: pstatx(is_directory)
            elif is_special_char: pstatx(is_special_char)
            elif is_block: pstatx(is_block)
            elif is_regular: pstatx(is_regular)
            elif is_fifo: pstatx(is_fifo)
            elif is_link: pstatx(is_link)
            elif is_sock: pstatx(is_sock)
            elif is_door: pstatx(is_door)
            elif is_port: pstatx(is_port)
            elif is_whiteout: pstatx(is_whiteout)
            elif is_mode: pstatx(is_mode)
            elif file_type: pstatx(file_type)
            elif protection_bits: pstatx(protection_bits)
            elif inode_number: pstatx(inode_number)
            elif device: pstatx(device)
            elif hard_links: pstatx(hard_links)
            elif user_id: pstatx(user_id)
            elif group_id: pstatx(group_id)
            elif byte_size: pstatx(byte_size)
            elif recent_access: pstatx(recent_access)
            elif recent_modification: pstatx(recent_modification)
            elif metadata_change: pstatx(metadata_change)
            elif atime_ns: pstatx(atime_ns)
            elif mtime_ns: pstatx(mtime_ns)
            elif ctime_ns: pstatx(ctime_ns)
            elif allocated_blocks: pstatx(allocated_blocks)
            elif filesystem_blocksize: pstatx(filesystem_blocksize)
            elif type_of_device: pstatx(type_of_device)
            elif login_name: pstatx(login_name)
            elif optional_encrypted_password: pstatx(iptional_encrypted_password)
            elif name_field: pstatx(name_field)
            elif home_directory: pstatx(home_directory)
            elif user_command_interpreter: pstatx(user_command_interpreter)
            elif file_mode: pstatx(file_mode)
            elif if_sock: pstatx(if_sock)
            elif if_link: pstatx(if_link)
            elif if_regular: pstatx(if_regular)
            elif if_block: pstatx(if_block)
            elif if_directory: pstatx(if_directory)
            elif if_special_char: pstatx(if_special_char)
            elif if_fifo: pstatx(if_fifo)
            elif is_uid: pstatx(is_uid)
            elif is_gid: pstatx(is_gid)
            elif sticky_bit: pstatx(sticky_bit)
            elif mask_owner_perm: pstatx(mask_owner_perm)
            elif owner_read: pstatx(owner_read)
            elif owner_write: pstatx(owner_write)
            elif owner_execute: pstatx(owner_execute)
            elif owner_full: pstatx(owner_full)
            elif mask_group_perm: pstatx(mask_group_perm)
            elif group_read: pstatx(group_read)
            elif group_write: pstatx(group_write)
            elif group_execute: pstatx(group_execute)
            elif group_full: pstatx(group_full)
            elif mask_others_perm: pstatx(mask_others_perm)
            elif others_read: pstatx(others_read)
            elif others_write: pstatx(others_write)
            elif others_execute: pstatx(others_execute)
            elif others_full: pstatx(others_full)
            elif system_lock: pstatx(system_lock)
            elif owner_v7_read: pstatx(owner_v7_read)
            elif owner_v7_write: pstatx(owner_v7_write)
            elif owner_v7_execute: pstatx(owner_v7_execute)
            elif owner_v7_full: pstatx(owner_v7_full)
            elif operating_system: pstatx(operating_system)
            elif cwd: pstatx(cwd)
            elif get_login: pstatx(get_login)

            else:
                usage()

        except (UnboundLocalError):
            pass

        except (TypeError):
            pass


if __name__ == "__main__":
        main()
