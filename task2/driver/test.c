#include <linux/kernel.h> 
#include <linux/module.h> 
#include <linux/init.h> 
#include <linux/fs.h>
#include <asm/uaccess.h> 

MODULE_LICENSE( "GPL" );
MODULE_AUTHOR( "Sergey Astakhov <fzastahov@gmail.com>" );
MODULE_DESCRIPTION( "My nice module" );
// MODULE_SUPPORTED_DEVICE( "test" ); /* /dev/testdevice */

#define SUCCESS 0
#define DEVICE_NAME "test" 

static int device_open( struct inode *, struct file * );
static int device_release( struct inode *, struct file * );
static ssize_t device_read( struct file *, char *, size_t, loff_t * );

static int major_number; 
static int is_device_open = 0; 
static int counter = 0;

static struct file_operations fops =
 {
  .read = device_read,
  .open = device_open,
  .release = device_release
 };

static int __init test_init( void )
{
 printk( KERN_ALERT "TEST driver loaded!\n" );
 major_number = register_chrdev( 0, DEVICE_NAME, &fops );

 if ( major_number < 0 )
 {
  printk( "Registering the character device failed with %d\n", major_number );
  return major_number;
 }
 
 // printk( "Test module is loaded!\n" );
 printk( "Please, create a dev file with 'mknod /dev/test c %d 0'.\n", major_number );
 return SUCCESS;
}

static void __exit test_exit( void )
{
 unregister_chrdev( major_number, DEVICE_NAME );

 printk( KERN_ALERT "Test module is unloaded!\n" );
}

module_init( test_init );
module_exit( test_exit );

static int device_open( struct inode *inode, struct file *file )
{
 printk( "Open driver tick.\n" );

 if ( is_device_open )
  return -EBUSY;

 is_device_open++;

 return SUCCESS;
}

static int device_release( struct inode *inode, struct file *file )
{
 printk( "Release driver tick.\n" );
 is_device_open--;
 return SUCCESS;
}

static ssize_t device_read(struct file *filp, char *buffer, size_t length,
			   loff_t *offset)
{
	//size_t read = sprintf(buffer, "%d\n", counter++);
    //return read;

    sprintf(buffer, "%d\n", counter++);
    printk( "Read driver tick.\n" );
    put_user( counter , buffer);
    return counter;
}