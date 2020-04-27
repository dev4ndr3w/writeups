#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <errno.h>
#include <seccomp.h>

int main()
{
	scmp_filter_ctx ctx = seccomp_init(SCMP_ACT_KILL_THREAD);
	if (ctx == (void *)0x00){
		puts("seccomp error");
		exit(0);
	}
	seccomp_rule_add(ctx, SCMP_ACT_ALLOW, 0xad, 0); // sys_rt_sigreturn
	seccomp_rule_add(ctx, SCMP_ACT_ALLOW, SCMP_SYS(open), 0);    // sys_open
	seccomp_rule_add(ctx, SCMP_ACT_ALLOW, SCMP_SYS(read), 0);    // sys_read
	seccomp_rule_add(ctx, SCMP_ACT_ALLOW, SCMP_SYS(write), 0);    // sys_write
	seccomp_rule_add(ctx, SCMP_ACT_ALLOW, SCMP_SYS(exit_group), 0); // sys_exit_group
	if(seccomp_load(ctx) < 0){
		seccomp_release(ctx);
		puts("seccomp error");
		exit(0);
	}

	__asm__ __volatile__ (
	"movl $0xad, %eax;"
	"int $0x80;"
	);
	seccomp_release(ctx);	
}
